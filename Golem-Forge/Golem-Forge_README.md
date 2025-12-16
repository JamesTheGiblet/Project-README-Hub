## **Build Log: The Golem's Forge - A Massive CoreXY 3D Printer**

### **The Problem**

Off-the-shelf 3D printers are toys. Their build volumes are too small for real, large-scale projects, and their frames are too flimsy for high-speed, precision work. I needed a machine that could print huge, functional parts without taking weeks to do it.

---

### **The Solution**

Build a monster. A printer with a **1.2 cubic meter build volume** built on a rock-solid extruded aluminum frame. The whole thing is designed around a **CoreXY movement system** because it's fast, precise, and scales up beautifully. This isn't a desktop toy; it's a fabrication tool.

---

### **Project Goals**

This build had a clear checklist:
* Build a huge, rigid frame (2m x 2m x 3m) that won't wobble.
* Use a CoreXY system for high-speed, accurate movement.
* Integrate a high-flow hotend that can lay down a lot of plastic, fast.
* Design a large heated bed that doesn't need a massive, dedicated power supply.
* Use off-the-shelf, reliable components like a Raspberry Pi for the brains.
* Make sure it's easy to upgrade later.

---

### **How It Works (The Guts)**

The system is straightforward. A **Raspberry Pi** and a **mini 5 Plus** board run the show. They read sensor data, process the G-code, and fire commands to the motors and heaters.



* **Controller:** The Raspberry Pi handles the processing and the touchscreen UI.
* **Movement:** The CoreXY system uses two long belts to control the X and Y axes. It's lighter and faster than moving the whole gantry. We're using **sensorless homing** and stall detection, so there are fewer wires and failure points.
* **Extrusion:** A **Hemera high-flow hotend** with a big **1.4mm Revo nozzle** pushes out a ton of plastic, which is essential for large prints.
* **Heated Bed:** The 1.2m x 1.2m build plate is too big to heat with a single power supply. So, it's actually **four separate beds**, each on its own mains-powered relay. The software only heats the sections needed for the print, saving power and time.

---

### **The Parts List (Bill of Materials)**

| Component | Spec / Note |
| :--- | :--- |
| **Frame** | 2m x 2m x 3m Extruded Aluminum |
| **Movement** | CoreXY System |
| **Controller** | Raspberry Pi A+ & Mini 5 Plus |
| **Display** | 5.5-inch Touchscreen |
| **Hotend** | Hemera High-Flow w/ 1.4mm Revo Nozzle |
| **Bed Leveling**| Automatic Bed Leveling Probe |
| **Heated Bed** | 4x independently powered beds on relays |
| **Homing** | Sensorless homing via stall detection |

---

### **The Brains (Software)**

* **The Setup:** It runs Raspberry Pi OS. The control scripts are written in **Python** because it's fast to prototype and there are tons of libraries for GPIO control.
* **The Print Job Workflow:**
    1.  **Boot Up:** The Pi starts, and the touchscreen shows the main controls.
    2.  **Load File:** You load a G-code file.
    3.  **Prep:** The printer runs its auto-leveling sequence.
    4.  **Smart Bed Heating:** The software reads the G-code to see how big the print's first layer is, then only turns on the bed sections it needs.
    5.  **Print:** The CoreXY system gets to work.
    6.  **Done:** You get a notification when it's finished.

---

### **What's Next (Future Upgrades)**

**Perfect is the imaginary friend of never shipped**, but there's always room for improvement.
* **Camera Monitoring:** Add a camera and some simple AI failure detection.
* **Predictive Maintenance:** Use motor current data to predict when bearings or belts need to be replaced.
* **Web Interface:** Build a simple web UI for remote control and monitoring.

**The build is the proof.** Now, let's print something huge.
