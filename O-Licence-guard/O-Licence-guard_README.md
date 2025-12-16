# O-Licence Guard (Bicester/Oxfordshire Edition)

## 🚛 Driver Readiness & Fatigue Visualizer for the M40 Corridor

**O-Licence Guard** is a localized digital safety tool designed specifically for HGV operators based in Bicester and the surrounding Oxfordshire area. It helps drivers visualize their fatigue levels before starting a shift, taking into account specific local traffic stressors like the A41 and M40 J9.

---

### 🎯 The Problem

Transport Managers know that "8 hours of sleep" isn't the only factor in driver fatigue. A driver starting a shift knowing they have to tackle **Bicester Village traffic** or **A41 congestion** starts with a higher cognitive load than a driver on an open road.

Standard telematics track the truck. This tool tracks the **driver**.

### 🛠 Key Features

#### **1. Hyper-Local Stress Factors**

Unlike generic fatigue apps, this tool includes presets for Bicester-specific hazards:

* **🛑 A41 Congestion:** Applies a penalty for the stop-start stress of the A41 dual carriageway.
* **🛍️ Bicester Village Rush:** Accounts for the high-alertness required during tourist peak times.
* **🚛 M40 J9 Delays:** Models the frustration/fatigue impact of the interchange.
* **⏱️ Warehouse Wait:** Factors in the lethargy caused by long waits at local distribution centers.

#### **2. Visual "Fit to Drive" Curve**

* Uses a **Pharmacokinetic Decay Model** (similar to caffeine half-life) to predict alertness over a 15-hour shift.
* Visualizes the exact hour a driver might drop below the "Safe Threshold."
* **Red/Amber/Green** status banners give an instant Go/No-Go decision.

#### **3. Zero Friction Deployment**

* **No App Store:** Runs instantly in any mobile browser (Chrome/Safari).
* **No Login:** Drivers don't need to remember passwords.
* **Offline Capable:** The core logic runs locally on the device.

---

### 🚀 How It Works

1. **Input Sleep:** Driver slides the bar to set hours slept in the last 24h.
2. **Select Hazards:** Driver taps local factors (e.g., "Night Trunk" + "A41 Congestion").
3. **View Curve:** The graph updates instantly to show the predicted fatigue curve for the shift ahead.
4. **Self-Declaration:** If the score is safe, the driver can check the declaration box to log their readiness.

---

### 🛡️ Protecting the O-Licence

This tool serves as a proactive measure for **FORS / DVSA compliance**:

* Demonstrates a commitment to managing driver fatigue beyond simple tachograph hours.
* Encourages drivers to take ownership of their fitness to drive.
* Reduces the risk of fatigue-related incidents on the A34/M40.

---

### 🔧 Technical Specs

* **Platform:** Progressive Web App (PWA).
* **Compatibility:** iOS, Android, Desktop.
* **Data Privacy:** No personal data is stored on external servers in this Lite version.

---

### 📄 License

**Proprietary Software** developed for the Bicester Logistics Community.
*Concept & Development by James Gilbert.*
