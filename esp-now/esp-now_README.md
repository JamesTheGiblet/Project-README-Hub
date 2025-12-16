
# ESP32 Bot Swarm Communication

## Overview

This project demonstrates how to set up wireless communication for a swarm of ESP32-based bots. It is broken down into two parts:

1. **Direct Wi-Fi Communication:** Establishes a stable, two-way link between a single ESP32 bot and a browser-based Master Control Program (MCP) using WebSockets and ESP-NOW.
2. **ESP-NOW Integration:** Expands on the first part by adding ESP-NOW for fast, local, bot-to-bot communication, creating a true swarm.

- 2 or more ESP32 development boards
- USB cables for programming

## Software Requirements

- Visual Studio Code (VS Code)
- PlatformIO extension for VS Code
- ESP32 board support via PlatformIO
- `ArduinoWebsockets` library by Markus Sattler (add to `platformio.ini`)

## Setup Instructions

1. **Install VS Code**: Download and install from <https://code.visualstudio.com/>
2. **Install PlatformIO Extension**: In VS Code, go to Extensions and search for "PlatformIO IDE". Install it.
3. **Create a New PlatformIO Project**:

- Click the PlatformIO icon in the VS Code sidebar.
- Select "New Project", choose your ESP32 board, and set the framework to Arduino.

1. **Add Required Libraries**:

- Open your project's `platformio.ini` file.
- Add the following line under `[env]` to include the ArduinoWebsockets library:
    `lib_deps = ArduinoWebsockets`

1. **Find MAC Addresses (for Part 2)**: Each ESP32 has a unique MAC address required for ESP-NOW. Upload the following utility sketch to each of your ESP32s and note down their addresses from the Serial Monitor.

   ```cpp
   #include <WiFi.h>

   void setup(){
     Serial.begin(115200);
     WiFi.mode(WIFI_STA);
     Serial.print("ESP32 Board MAC Address:  ");
     Serial.println(WiFi.macAddress());
   }
   void loop(){}
   ```

## Part 1: Direct Wi-Fi Communication (MCP to Single Bot)

This first step focuses on creating a stable, two-way communication channel between a single ESP32 bot and the `MCP.html` GUI, which will act as our Master Control Program (MCP). We will use WebSockets for a persistent, low-latency connection directly over your local Wi-Fi network.

**Note:** All code examples in this README are compatible with PlatformIO. Simply copy the code into your project's `src` folder and build/upload using PlatformIO.

### Architecture (Part 1)

- **ESP32 Bot:** Connects to your Wi-Fi and runs a WebSocket server. It periodically sends its status (e.g., sensor data, energy level) to any connected client. It also listens for incoming messages (commands) from the client and can communicate with other bots using ESP-NOW.
- **MCP (Browser):** You open the `MCP.html` file in your browser. The JavaScript in the file connects to the ESP32's WebSocket server. It visualizes the data received from the bot and provides UI elements to send commands back.

### ESP32 WebSocket Server Code

Upload the following code to your ESP32. **Remember to update your Wi-Fi credentials.**

```cpp
#include <WiFi.h>
#include <ArduinoWebsockets.h>

// --- Configuration ---
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const int websocket_port = 81; // Port for the WebSocket server

WebsocketsServer server;

// --- Bot State ---
int bot_id = 1;
float x = 50.0, y = 50.0;
int energy = 100;
String state = "idle";

// Function to handle incoming WebSocket messages
void onMessage(WebsocketsClient &client, WebsocketsMessage message) {
    Serial.print("Received command from MCP: ");
    Serial.println(message.data());

    // Example command handling
    if (message.data() == "move") {
        state = "moving";
    } else if (message.data() == "stop") {
        state = "idle";
    }

    // Echo the command back to the client for confirmation
    client.send("Command received: " + message.data());
}

// Function to handle WebSocket events
void onEvent(WebsocketsClient &client, WebsocketsEvent event, String data) {
    if (event == WebsocketsEvent::Connection) {
        Serial.println("MCP connected!");
    } else if (event == WebsocketsEvent::Disconnection) {
        Serial.println("MCP disconnected.");
    }
}

void setup() {
    Serial.begin(115200);

    // Connect to Wi-Fi
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi...");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi Connected.");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());

    // Setup WebSocket server
    server.listen(websocket_port);
    Serial.printf("WebSocket server started on port %d\n", websocket_port);

    // Assign callbacks
    server.onMessage(onMessage);
    server.onEvent(onEvent);
}

void loop() {
    // This is required for the library to process incoming messages
    server.poll();

    // Periodically send bot status to all connected clients (the MCP)
    static unsigned long lastSendTime = 0;
    if (millis() - lastSendTime > 1000) {
        lastSendTime = millis();

        // Simulate bot movement and energy drain
        if (state == "moving") {
            x += (random(-5, 6));
            y += (random(-5, 6));
            energy -= 1;
            if (energy < 0) energy = 0;
        }

        // Create a JSON string with the bot's status
        String jsonStatus = "{\"id\":" + String(bot_id) +
                            ",\"x\":" + String(x) +
                            ",\"y\":" + String(y) +
                            ",\"energy\":" + String(energy) +
                            ",\"state\":\"" + state + "\"}";

        // Broadcast the status to all connected clients
        server.broadcast(jsonStatus);
        Serial.println("Sent status to MCP: " + jsonStatus);
    }
}
```

## Usage

1. Get the MAC address of each ESP32 using the sketch in the Setup Instructions.
2. In the main example code, update the `peerAddress` variable with the MAC address of the *other* ESP32.
3. Upload the modified code to each respective ESP32 board.
4. Open a Serial Monitor for each board (baud rate: 115200).
5. You will see the devices exchanging data every two seconds. The sender will report send status, and the receiver will print the contents of the structured data it receives.

## Advanced: Architecture with Master Control Program (MCP)

For more complex scenarios, you can introduce a PC-based Master Control Program that acts as a passive observer and mild influencer. The ESP32 bots communicate with each other using ESP-NOW for low-latency local messaging, while a dedicated **Gateway ESP32** bridges this network to your local Wi-Fi, allowing the MCP to interact with the swarm.

**Architecture:**

1. **Bot ESP32s:** Standard swarm members. They run on ESP-NOW, sending status updates and listening for commands. They only know about other ESP-NOW peers.
2. **Gateway ESP32:** A special bot that is connected to both the ESP-NOW network and your home/office Wi-Fi. It forwards messages from the bots to the MCP and relays commands from the MCP back to the bots.
3. **PC / Master Control Program (MCP):** A computer on the same Wi-Fi network. It runs a backend service (e.g., a Node.js script) to listen for UDP packets from the Gateway. This backend can then visualize the data (using a tool like your `MCP.html`) and send command packets back to the Gateway.

### Gateway ESP32 Code

This code connects to your Wi-Fi and listens for UDP packets from the MCP while also participating in the ESP-NOW network.

```cpp
// GATEWAY ESP32 CODE
#include <WiFi.h>
#include <WiFiUdp.h>
#include <esp_now.h>

// Wi-Fi Credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// UDP settings
WiFiUDP udp;
const int udpPort = 12345; // Port to listen on
IPAddress remoteIp(192, 168, 1, 100); // REPLACE WITH YOUR PC's IP ADDRESS

// Define a data structure for bot-to-bot and bot-to-mcp communication
typedef struct struct_message {
    int id;
    float x, y;
    int energy;
    char message[32];
} struct_message;

struct_message incomingData;

// MAC Address of the broadcast peer (all other bots)
uint8_t broadcastAddress[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};

// Callback when data is received via ESP-NOW
void OnDataRecv(const uint8_t * mac, const uint8_t *data, int len) {
  // Forward received ESP-NOW data to the MCP via UDP
  udp.beginPacket(remoteIp, udpPort);
  udp.write(data, len);
  udp.endPacket();
  Serial.println("Forwarded ESP-NOW packet to MCP.");
}

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.mode(WIFI_AP_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected.");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Initialize ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  esp_now_register_recv_cb(OnDataRecv);

  // Register broadcast peer for sending commands
  esp_now_peer_info_t peerInfo;
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }

  // Start listening for UDP packets
  udp.begin(udpPort);
  Serial.printf("Listening for UDP packets on port %d\n", udpPort);
}

void loop() {
  // Check for UDP packets from MCP
  int packetSize = udp.parsePacket();
  if (packetSize) {
    // Read the packet into a buffer
    uint8_t packetBuffer[255];
    int len = udp.read(packetBuffer, 255);
    if (len > 0) {
      // Broadcast the received packet to all ESP-NOW peers
      esp_now_send(broadcastAddress, packetBuffer, len);
      Serial.println("Relayed command from MCP to ESP-NOW swarm.");
    }
  }
}
```

### MCP Backend (Node.js Example)

Save this as `server.js` on your PC. It listens for data from the Gateway and allows you to send a command back by typing in the console.

```javascript
// server.js
const dgram = require('dgram');
const readline = require('readline');
const server = dgram.createSocket('udp4');

const GATEWAY_IP = '192.168.1.150'; // REPLACE WITH YOUR GATEWAY's IP
const GATEWAY_PORT = 12345;

server.on('error', (err) => {
  console.log(`Server error:\n${err.stack}`);
  server.close();
});

server.on('message', (msg, rinfo) => {
  // Assuming msg is a buffer containing the struct_message
  // You would parse this buffer based on your C++ struct layout
  console.log(`Received data from ${rinfo.address}:${rinfo.port}`);
  // Example: a simple text message from a bot
  console.log(`Bot Message: ${msg.toString('utf8', 12, 44)}`); // Bytes 12-44 for the char[32]
});

server.on('listening', () => {
  const address = server.address();
  console.log(`UDP Server listening on ${address.address}:${address.port}`);
});

server.bind(12345); // Must match the port on the Gateway

// Allow sending commands from the console
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
rl.on('line', (input) => {
    // Create a buffer that matches the struct_message to send a command
    const command = { id: 0, x: 0, y: 0, energy: 0, message: input };
    const buffer = Buffer.alloc(44); // sizeof(struct_message)
    buffer.writeInt32LE(command.id, 0);
    buffer.writeFloatLE(command.x, 4);
    buffer.writeFloatLE(command.y, 8);
    buffer.writeInt32LE(command.energy, 12);
    buffer.write(command.message, 16, 32, 'utf8');

    server.send(buffer, GATEWAY_PORT, GATEWAY_IP, (err) => {
        if (err) console.error(err);
        else console.log(`Command "${input}" sent to gateway.`);
    });
});
```

## References

- [ESP-NOW Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html)
- [Arduino ESP32](https://github.com/espressif/arduino-esp32)
- [ArduinoWebsockets Library](https://github.com/Links2004/arduinoWebSockets)
