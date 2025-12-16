# PinPoint Planner Pro

![SBC Example](https://upload.wikimedia.org/wikipedia/commons/3/3d/Raspberry_Pi_4_Model_B_-_Side.jpg)

**Your professional toolkit for planning hardware projects without the headache.**

*PinPoint Planner is an intelligent, web-based tool for designing projects with single-board computers like Raspberry Pi, Arduino, and ESP32. Go from idea to a validated, documented plan in minutes, not hours.*

---

## Table of Contents

- [The Problem You've Faced](#the-problem-youve-faced)
- [The Intelligent Solution](#the-intelligent-solution)
- [Screenshots](#screenshots)
- [Prerequisites](#prerequisites)
- [Supported Hardware](#supported-hardware)
- [Adding More Components](#adding-more-components)
- [Development Tips](#development-tips)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

---

## The Problem You've Faced

If you've ever worked with an SBC, you know the frustration:

- **Endless Pin Puzzles:** Which GPIO can I use? Is this pin for I²C or SPI? Wait, I used that one already...
- **Datasheet Overload:** Dozens of open browser tabs, trying to reconcile board pinouts with component requirements.
- **Costly Mistakes:** A wrong connection or voltage mismatch leads to frustrating debugging or fried components.
- **Messy Documentation:** Final plans are often disorganized, making them hard to share or reproduce.

This process is slow, error-prone, and stifles creativity.

---

## The Intelligent Solution

PinPoint Planner transforms this process into a fast, visual, and reliable workflow. It's your single source of truth for hardware design.

- **Plan Visually:** See your board's pins in real-time. As you add components, the planner shows you exactly what's available.
- **Get Instant Validation:** Our intelligent core automatically flags issues, preventing conflicts before they happen.
- **Generate Docs in One Click:** Export a clean, professional summary of your project, including a component list and pin assignments.
The Pin Validator is like a real-time spell-checker for your hardware:
- **Catches Conflicts:** Instantly flags if a pin is already in use.
- **Prevents Mismatches:** Warns if you try to connect a component to an incompatible bus.
- **Stops Errors Before They Happen:** Ensures every manual connection is valid.

### 2. AI Smart Planner

- **One-Click Planning:** Add all your components, click "Plan My Board," and the AI gets to work.
- **Holistic Optimization:** Finds the best pin assignments, prioritizing stable hardware buses and respecting power constraints.
- **Explainable Decisions:** Tells you why it made each choice, so you learn and stay in control.

---

## Find Your Plan: From Free to Pro

| Feature                | Free (Simple Projects) | Pro ($7/mo) (Hobbyists & Power Users) | Business ($25/mo/seat) (Teams & Professionals) |
|------------------------|:---------------------:|:-------------------------------------:|:----------------------------------------------:|
| Projects               | Unlimited Local Projects | Unlimited Public & Private Projects   | Unlimited Team Projects                        |
| Core Planner           | ✅                    | ✅                                    | ✅                                             |
| Intelligence           | Pin Validator         | ⭐ AI Smart Planner                   | ⭐ AI Smart Planner                            |
| Documentation          | Markdown Export       | PDF & JSON Export                    | Custom Templates                              |
| Wiring Diagrams        | ✅ Text-based Instructions | ✅ Fritzing-style Diagrams            | ✅ Advanced Diagrams                          |
| Code Generation        | ✅ Arduino/Python Starter Code | ✅ Arduino/Python Starter Code        | ✅ Custom Code Templates                      |
| Bill of Materials (BOM)  | ✅ Copy as Text       | ✅ Export to CSV                       | ✅ Export to CSV                               |
| Custom Components      | ✅ (Up to 5)          | ✅ Unlimited Custom Components        | ✅ Shared Team Library                        |
| Collaboration          | ❌                    | ❌                                   | ✅ Real-time Editing                          |

---

## Features

| Feature | Description | Free | Pro | Business |
| :--- | :--- | :---: | :---: | :---: |
| **Core Visual Planner** | Drag-and-drop components onto interactive board diagrams. | ✅ | ✅ | ✅ |
| **Pin Validator** | Get real-time feedback on pin compatibility and conflicts. | ✅ | ✅ | ✅ |
| **Project Management** | Save projects locally in your browser. | ✅ (3) | ✅ (Unlimited) | ✅ (Team) |
| **Basic Export** | Download or copy your project plan as a clean Markdown file. | ✅ | ✅ | ✅ |
| **AI Smart Planner** | Automatically generate an optimized, conflict-free pin layout. | ❌ | ⭐ | ⭐ |
| **Advanced Exports** | Export to JSON for data interchange and professional PDF documents. | ❌ | ✅ | ✅ |
| **Wiring Diagrams** | Generate and copy text-based wiring instructions. | ✅ | ✅ (Graphical) | ✅ (Advanced) |
| **Bill of Materials** | Generate a shopping list and copy it as text. | ✅ | ✅ (CSV Export) | ✅ (CSV Export) |
| **Code Generation** | Get starter code in Arduino (C++) and Python. | ✅ | ✅ | ✅ (Custom) |
| **Custom Components** | Create and save your own components to a personal library. | ✅ (Up to 5) | ✅ (Unlimited) | ✅ (Shared) |
| **Real-time Collaboration** | Work on projects with your team simultaneously. | ❌ | ❌ | ✅ |

---

## Screenshots

*Application screenshots will be added here.*

**Pin Validator in Action (Free Tier):**

```text
┌──────────────────────────────────────────────────────────────┐
│ 🔴 Error: Pin Conflict!                                      │
│ Pin 3 (SDA) is already assigned to BMP280.                   │
└──────────────────────────────────────────────────────────────┘
```

---

## Prerequisites

- A modern web browser (Chrome, Firefox, Edge, etc.)
- A local web server to serve the files (e.g., [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension for VS Code)

### Running Locally

```bash
git clone https://github.com/your-username/pinpoint-planner.git
cd pinpoint-planner
```

Open `index.html`:

- With Live Server: Right-click `index.html` and choose "Open with Live Server".
- Or open `index.html` directly in your browser.

---

## Supported Hardware

| Family        | Supported Boards         | Status     |
|---------------|-------------------------|------------|
| Raspberry Pi  | Pi 4B, Pi 3B+           | ✅ Supported |
| Arduino       | Uno R3, Nano            | ✅ Supported |
| ESP           | ESP32 DevKit            | ⏳ Coming Soon |

---

## Adding More Components

You can expand your component library in two ways:

### 1. Manually Add a Component

To add a single new component, you can add its definition directly to the `componentData` object in `data/components.js`.

### 2. Import a Component Pack

You can import a JSON file containing multiple component definitions. In the "Add Components" section of the sidebar, click the "Import" icon (📁) and select your component pack file. The new components will be added and saved in your browser for future sessions.

**Component Template:**

The following shows the structure for a single component definition. Each field is explained with comments and an example for a simple LED.

```javascript
// A unique, machine-readable ID for the component (e.g., 'bmp280', 'led-red-5mm').
'example-component-id': {
  // The user-facing name of the component.
  name: 'Red LED (5mm)',

  // A FontAwesome 5 icon class for the UI (e.g., 'fas fa-lightbulb').
  icon: 'fas fa-lightbulb',

  // A short description that appears on hover.
  tip: 'A simple 5mm red Light Emitting Diode. Requires a current-limiting resistor.',

  // An array of supported voltage levels. This enables validation against board pin voltages.
  // Examples: ['3.3V'], ['5V'], ['3.3V', '5V']
  voltage: ['3.3V', '5V'],

  // An array of pin objects defining the component's connection requirements.
  // This is the most important part for the planner.
  pins: [
    {
      // The name of the pin on the component itself (e.g., "Anode", "SDA", "VIN").
      name: 'Anode',
      // The type of board pin it must connect to.
      // Valid types: 'gpio', 'power', 'ground', 'sda', 'scl', 'mosi', 'miso', 'sclk', 'cs', 'tx', 'rx'
      type: 'gpio'
    },
    {
      name: 'Cathode',
      type: 'ground'
    }
  ],

  // Optional: An array of other component IDs that this component needs to function.
  // e.g., a specific sensor might require a 'level-shifter' component.
  dependencies: ['resistor-220-ohm'],

  // Optional: Important notes for the user, displayed in the final project documentation.
  notes: 'A 220Ω resistor is recommended when connecting to a 3.3V GPIO pin.'
}
```

To add new boards, extend the `boardData` object with new board definitions, including pin layouts and specifications.

---

## Development Tips

- **Components not appearing:** Check the browser console for JavaScript errors.
- **Drag & drop not working:** Ensure touch polyfill is loaded.
- **Images not loading:** Verify image paths and file existence.
- **Export not working:** Check browser permissions for file downloads.

### Testing

This project uses QUnit for unit testing. To run the tests:

1. Make sure you are running the project from a local web server (like VS Code's Live Server).
2. Navigate to the `/tests/tests.html` file in your browser.

**Browser Requirements:**

- Modern browser with ES6 support
- File download permissions for export features
- Local storage for project saving

**Next Steps:**

- Add missing images for boards (`images/Raspberry Pi 4B.png`, `images/arduino_schematics_pins.png`, `images/ESP32_schematics_pins.png`)
- Test all functionality thoroughly
- Consider adding more board types (Arduino Nano, ESP8266, etc.)
- Implement user feedback from testing
- Plan Pro features development timeline

---

## Contributing

This project thrives on community contributions! Whether it's adding a new board, a new component, or improving the code, your help is welcome.

Please read our `CONTRIBUTING.md` for details on our code of conduct, development process, and how to submit a pull request. The easiest way to help is to add new hardware definitions!

---

## Roadmap

- ✅ **Phase 1: Core Platform** – Visual planner with Pin Validator, basic docs.
- ✅ **Phase 2: Pro Tier** – AI Smart Planner, wiring diagrams, code generation, custom components.
- 🚀 **Phase 3: Business Tier** – User accounts, real-time collaboration, and organizational features.
- ⏳ **mod packs** – Expand the component library with user-generated content.
- 💼 **White-Label Solutions** – Custom-branded versions of the planner for specific products or companies.
- 🛠️ **Ongoing** – Bug fixes, performance improvements, and user-requested features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
