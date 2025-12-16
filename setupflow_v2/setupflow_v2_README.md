# Hardware Onboarding Flow Component

A production-ready React component for creating guided hardware setup and onboarding flows with **external YAML/JSON configuration support**. Perfect for IoT devices, smart home hubs, industrial equipment, and any hardware that needs a structured setup process.

## 🚀 Features

### Core Features

- **Step-by-step guided onboarding** with dependency management
- **Real-time sensor monitoring** with customizable thresholds
- **Progress tracking** with visual indicators and timers
- **Toast notifications** for user feedback and status updates
- **Responsive design** that works on desktop and mobile
- **Accessibility** support with proper ARIA labels and keyboard navigation

### Production-Ready Features

- **🔧 External Configuration Loading**: Load setup flows from YAML or JSON files
- **📝 JSON Schema Validation**: Ensure configuration integrity with comprehensive validation
- **🔄 Dynamic Config Switching**: Change configurations without rebuilding
- **⚡ Performance Optimized**: Efficient loading and caching of external configs
- **🛡️ Error Handling**: Graceful handling of config loading failures
- **📊 Config Validation**: Detailed validation with helpful error messages

## 📦 Installation

```bash
# Clone the repository
git clone <repository-url>
cd SetupFlow

# Install dependencies
npm install

# Start development server
npm run dev
```

## 🔧 Configuration-Driven Architecture

The component supports loading configurations from external YAML or JSON files, making it highly reusable across different hardware types and setup processes.

### Basic Usage with External Config

```jsx
import HardwareOnboardingDemo from './HardwareOnboardingDemo'

// Load config from external file
function App() {
  return (
    <HardwareOnboardingDemo 
      configUrl="/path/to/your-config.yaml"
    />
  )
}
```

### Configuration File Structure

#### YAML Example (`example-config.yaml`)

```yaml
metadata:
  title: "Smart Home Hub Setup"
  description: "Complete setup process for your smart home hub"
  version: "1.0.0"
  estimatedDuration: 15

settings:
  showProgress: true
  allowSkipping: false
  showTimer: true
  showSensorData: true

steps:
  - id: "welcome"
    title: "Welcome to Your Smart Home Hub"
    description: "Let's get your device set up"
    type: "welcome"
    duration: 2
    requirements: []
    actions:
      - type: "info"
        content: "Please ensure your device is connected to power"

  - id: "sensors"
    title: "Sensor Calibration"
    description: "Calibrate environmental sensors"
    type: "calibration"
    duration: 5
    requirements: []
    sensors:
      - type: "temperature"
        name: "Temperature Sensor"
        unit: "°C"
        range: [18, 28]
        optimal: [20, 24]
      - type: "humidity"
        name: "Humidity Sensor"
        unit: "%"
        range: [30, 70]
        optimal: [40, 60]
```

#### JSON Example (`industrial-config.json`)

```json
{
  "metadata": {
    "title": "Industrial IoT Gateway Setup",
    "description": "Production-grade setup for industrial IoT gateway",
    "version": "2.1.0",
    "estimatedDuration": 25
  },
  "settings": {
    "showProgress": true,
    "allowSkipping": true,
    "showTimer": true,
    "showSensorData": true
  },
  "steps": [
    {
      "id": "power_check",
      "title": "Power System Verification",
      "description": "Verify power supply and backup systems",
      "type": "validation",
      "duration": 3,
      "requirements": [],
      "actions": [
        {
          "type": "power_validation",
          "instruction": "Checking main power supply and UPS backup system"
        }
      ]
    }
  ]
}
```

## Features Demonstrated

### 🔧 **Step Types**

- `checklist` - Interactive checklists with structured items
- `instruction` - Manual steps with images/videos  
- `automated` - Simulated hardware detection with progress indicators
- `calibration` - Sensor calibration with live data validation
- `completion` - Success screen with next steps

### 📊 **Live Sensor Dashboard**

- **Real-time data**: Voltage and distance readings update every 1.2 seconds
- **Status indicators**: Green/red borders show if readings are within expected ranges
- **Expected ranges**: Configurable per step (e.g., 4.5V-6.0V for power connection)

### 🔗 **Step Dependencies**

- **Dependency enforcement**: Later steps locked until prerequisites completed
- **Visual indicators**: Clear dependency status in navigation sidebar
- **Smart navigation**: Click-to-navigate respects dependency rules

### ⏱️ **Duration Tracking**

- **Per-step timing**: Real-time timer for each step
- **MM:SS format**: Easy-to-read duration display
- **Automatic reset**: Timer resets when moving to new step

### 🔄 **Validation & Recovery**

- **Sensor validation**: Automatic checks against expected ranges
- **Retry logic**: Configurable retry attempts with fallback steps
- **Error handling**: Toast notifications and user guidance

### 🎨 **User Experience**

- **Toast notifications**: Success/error messages with animations
- **Progress tracking**: Visual progress bar and step completion status
- **Responsive design**: Works on different screen sizes
- **Smooth animations**: Enhanced with Tailwind CSS transitions

---

## Example Configuration

```javascript
const exampleConfig = {
  onboarding: {
    title: "RoboKit Setup Guide",
    description: "Complete setup for your robotics kit",
    estimated_time: "20 minutes",
    steps: [
      {
        id: "detect_hardware",
        title: "Detect Hardware", 
        type: "automated",
        description: "Connect your RoboKit. We will automatically detect it.",
        detection_tasks: [
          { id: "scan_usb", label: "Scan USB Ports", icon: Usb },
          { id: "identify_device", label: "Identify RoboKit Pro", icon: Cpu },
          { id: "check_compatibility", label: "Check Compatibility", icon: ShieldCheck }
        ],
        validation: { type: "automated" }
      },
      {
        id: "connect_power",
        title: "Connect Power",
        type: "instruction", 
        description: "Connect the battery pack to the controller.",
        show_sensor_dashboard: true,
        media: {
          type: "image",
          url: "https://i.imgur.com/8x5xG4w.png",
          alt: "Battery connection diagram"
        },
        validation: { 
          type: "sensor_check", 
          sensor: "voltage_sensor", 
          expected_range: [4.5, 6.0] 
        }
      },
      {
        id: "firmware_upload",
        title: "Upload Firmware",
        type: "automated",
        description: "Automatically upload the latest firmware.",
        on_failure: {
          retry_count: 2,
          fallback_step: "manual_firmware_upload",
          error_message: "Automatic upload failed. Please try manual method."
        },
        validation: { type: "automated" }
      }
      // ... more steps
    ]
  }
};
```

---

## Custom Hooks

The demo showcases several React patterns:

### **useSensorData Hook**

```javascript
const { sensorData } = useSensorData();
// Returns: { voltage: 5.1, distance: 30.2 }
```

### **useStepTimer Hook**

```javascript
const stepDuration = useStepTimer(currentStepId);
// Returns: seconds elapsed since step started
```

### **useToasts Hook**

```javascript
const { toasts, addToast } = useToasts();
addToast('Hardware detected successfully!', 'info');
```

---

## Dependencies

The demo uses these dependencies defined in `stepDependencies`:

```javascript
const stepDependencies = {
  'connect_power': ['detect_hardware'],
  'firmware_upload': ['connect_power'], 
  'calibrate_sensors': ['firmware_upload']
};
```

This ensures users complete steps in the correct order.

---

## Tech Stack

- **React 18** - Component framework
- **Vite** - Development server and build tool
- **Tailwind CSS** - Styling and animations
- **Lucide React** - Icon library
- **JavaScript/JSX** - No TypeScript (keeping it simple)

---

## Project Structure

```txt
SetupFlow/
├── src/
│   └── main.jsx           # React app entry point
├── main.jsx               # Hardware onboarding component  
├── index.html            # HTML template with Tailwind CDN
├── package.json          # Dependencies and scripts
├── vite.config.js        # Vite configuration
└── README.md            # This file
```

---

## Key Components

### **SensorDashboard**

Displays live sensor readings with status indicators:

- Green border: readings within expected range
- Red border: readings outside expected range  
- Expected ranges shown for context

### **Step Navigation**

Interactive sidebar showing:

- Step completion status (✓ for completed)
- Current step highlighting
- Dependency requirements for locked steps
- Click-to-navigate (respects dependencies)

### **Toast Notifications**

Animated notifications for:

- Success messages (blue theme)
- Error messages (red theme)
- Auto-dismiss after 5 seconds
- Slide-in animations

---

## Demo Flow

1. **Unbox Components** - Checklist step
2. **Detect Hardware** - Automated detection simulation
3. **Connect Power** - Instruction with live voltage monitoring
4. **Upload Firmware** - Automated with retry logic
5. **Manual Firmware Upload** - Fallback step (if needed)
6. **Test Motors** - Interactive step
7. **Calibrate Sensors** - Live distance sensor monitoring
8. **Setup Complete** - Success screen with next steps

---

## Use Cases

This demo is useful for understanding patterns for:

- **Robotics kits** requiring assembly and sensor calibration
- **IoT devices** with multi-step WiFi setup and configuration  
- **Development boards** (Arduino, Raspberry Pi, ESP32) needing firmware and testing
- **Lab equipment** with complex initialization procedures
- **Manufacturing testing** with sensor validation workflows
- **Product onboarding** requiring step-by-step user guidance

---

## What You Can Learn

This demo showcases several important patterns:

### **Configuration-Driven UI**

- Define complex flows in data structures
- Separate presentation logic from flow logic
- Make flows easily modifiable without code changes

### **Real-Time Data Integration**

- Live sensor monitoring with status validation
- Expected vs actual value comparison
- Visual feedback for out-of-range conditions

### **State Management**

- Step completion tracking
- Dependency validation
- Progress persistence across navigation

### **Error Handling**

- Graceful retry mechanisms
- Fallback step routing
- User-friendly error messaging

### **Custom React Hooks**

- Reusable sensor data management
- Timer functionality
- Toast notification system

---

## Running the Demo

After starting with `npm run dev`, try these test scenarios:

1. **Complete Flow**: Go through all steps in order
2. **Dependency Testing**: Try clicking later steps before completing prerequisites  
3. **Sensor Validation**: Watch voltage/distance readings and validation logic
4. **Error Scenarios**: Test firmware upload failures and retry logic
5. **Navigation**: Use both sidebar navigation and previous/next buttons

---

## Architecture

```txt
Configuration Objects → React Component → Live Sensor Data
        ↓                     ↓                ↓
    Step Definitions → State Management → Validation Logic
        ↓                     ↓                ↓  
   Dependency Rules →  UI Components  → User Feedback
```

The demo shows how to build robust hardware onboarding experiences with:

- **Declarative configuration** for easy modification
- **Real-time data integration** for immediate feedback
- **Smart state management** for complex workflows
- **Professional UI/UX** for better user experience

---

## Limitations & Notes

This is a **demonstration/prototype** showing concepts:

- Sensor data is simulated (random values within realistic ranges)
- Hardware detection is mocked with animations  
- No actual hardware integration (framework for UI patterns)
- Validation logic is simplified for demo purposes
- No persistence across browser refreshes

For production use, you'd need to:

- Integrate with actual sensor APIs
- Add real hardware detection logic
- Implement proper state persistence
- Add comprehensive error handling
- Include accessibility features

---

## Potential Extensions

The patterns shown here could be extended with:

- **Database persistence** for setup progress
- **WebSocket integration** for real-time hardware communication
- **Plugin architecture** for different hardware types
- **Visual flow editor** for non-technical users
- **Template library** for common setup patterns
- **Multi-language support** for international products
- **Analytics integration** for setup completion tracking

---

## Contributing

This is a demonstration project. Feel free to:

- Fork and experiment with different configurations
- Add new step types or validation patterns
- Improve the UI/UX design
- Integrate with actual hardware for real-world testing

---

## License

MIT - Feel free to use these patterns in your own projects!
