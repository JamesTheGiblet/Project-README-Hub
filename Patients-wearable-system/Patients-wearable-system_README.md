## **Project: The Patient Watch System**

#### **The Problem**

Hospitals run on outdated systems and paper trails. Nurses are overworked, appointments run late, and there's no simple way to track where the real bottlenecks are. You can't fix what you can't measure. On top of that, ensuring patient safety—especially for those at risk of falling or wandering—is a constant challenge.

-----

#### **The Solution**

A simple, local-first tracking system using cheap smartwatches. Each patient gets a watch that does three things:

1.  **Tracks their location** inside the hospital for safety (geofencing).
2.  **Logs timing** for appointments and medication rounds to spot delays.
3.  **Lets them check in** with their mood and pain levels.

The data stays on-site and is owned by the patient. No cloud accounts, no selling data. Just a tool to make the hospital safer and more efficient.

-----

#### **How It's Put Together (The Architecture)**

It’s a simple setup. The watch talks to a local hub, and the hub feeds a dashboard for staff.

```mermaid
graph TD
    A[Patient's Smartwatch] --> B[Local Hub (Tablet/Pi)]
    B --> C[Encrypted Local Storage]
    B --> D[Staff Dashboard]
```

  * **The Watch:** Any cheap smartwatch with Bluetooth and GPS.
  * **The Hub:** A tablet or Raspberry Pi in the room or at the nurse's station. It's the brain that collects the data.
  * **The Dashboard:** A simple web page staff can see, showing alerts and a summary of the data.

-----

#### **The Rules & The Setup**

This has to be straightforward.

**The Rules (The "Consent" Part):**

  * **Location is for safety only.** The GPS is used to make sure you're in a safe area of the hospital.
  * **It's the hospital's property.** You're liable if you lose or break the watch.
  * **You can get a copy of your data.** When you're discharged, you can ask for an encrypted file of all your logs.

**The Setup (5-Minute Install):**

1.  Connect the watch to the local hub device.
2.  A nurse drags the patient's `.json` config file onto the hub's interface.
3.  The watch automatically syncs the patient's schedule and safety zones.
4.  The patient walks to a doorway to trigger a test alert.
5.  The patient gets a one-page guide on how the watch works.

-----

#### **What It Actually Tracks**

This system is about gathering useful data. **The code is the proof**, and the data doesn't lie.

##### **1. Appointment & Medication Delays**

Instead of guessing why the schedule is always off, the system logs it.

**The Plan (Config):**

```json
{
  "appointments": [
    {
      "type": "MRI Scan",
      "scheduled": "2025-08-10T14:00:00",
      "location": "Radiology Room 3"
    }
  ],
  "med_schedule": [
    {"med": "Lisinopril", "time": "08:00"}
  ]
}
```

**What Actually Happened (Logged Event):**

```json
{
  "appointment": "MRI Scan",
  "scheduled": "14:00",
  "started": "14:25",
  "delay_minutes": 25,
  "reason": "Machine calibration"
}
```

Now, instead of blaming staff, a manager can see the MRI machine is the real bottleneck.

##### **2. Patient Well-being Checks**

The watch prompts the patient with simple questions at set intervals.

**The Questions (Config):**

```json
{
  "checkup_interval_hours": 12,
  "questions": ["How are you feeling?", "Rate your pain (0–10)"]
}
```

**The Response (Logged Event):**

```json
{
  "timestamp": "2025-08-10T09:00:00",
  "mood": "Anxious",
  "pain_level": 6,
  "notes": "Woke up with headache"
}
```

If a patient's pain level is consistently rising, the dashboard can flag it for a nurse to check in.

-----

#### **What the Data Tells You (The Dashboard)**

The whole point of collecting data is to make it useful. The dashboard shows:

  * **Appointment Delays:** Which departments are the biggest bottlenecks?
  * **Medication Timing:** Are nurses overloaded at certain times of the day?
  * **Mood & Pain Trends:** Which patients might need extra attention?
  * **Geofence Alerts:** Are at-risk patients wandering near exits?

-----

#### **What's Next (Future Upgrades)**

**Perfect is the imaginary friend of never shipped**, but here's where this could go:

  * **Visitor Mode:** Grant temporary location access to a family member's phone.
  * **Discharge Mode:** Continue lightweight monitoring at home for a week post-discharge.
  * **AI Alerts:** Use the data to predict which patients are at a higher risk of a decline.
