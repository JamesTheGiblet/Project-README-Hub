# Procurement Suite

## 🚀 Strategic Sourcing & Inventory Optimization Toolkit

**Procurement Suite** is a bespoke web-based decision support system designed for Senior Engineering Buyers. It bridges the gap between complex spreadsheets and quick strategic decision-making, providing real-time visualization for "Make vs. Buy" scenarios and inventory optimization.

---

### 📊 Current Capabilities

#### **1. Make vs. Buy Analyzer**

* **The Problem:** Deciding whether to manufacture a component in-house (High NRE/Setup, Low Unit Cost) or outsource it (Low Setup, Higher Unit Cost).
* **The Solution:**
  * Visualizes the exact **Break-Even Quantity**.
  * Dynamically plots Total Cost curves for both scenarios.
  * Provides instant recommendations (e.g., *"If demand > 818 units, MAKE"*).

#### **2. Inventory Optimizer (EOQ)**

* **The Problem:** Balancing the cost of holding stock against the cost of placing frequent orders.
* **The Solution:**
  * Calculates the **Economic Order Quantity (EOQ)** based on annual demand, holding costs, and ordering fees.
  * Visualizes the "Total Cost Curve" to show the sweet spot for cash flow efficiency.
  * Calculates optimal order frequency (Orders Per Year).

---

### 🔮 Future Enhancements Roadmap

We are actively developing V2.0 to further integrate with the supply chain workflow. Planned features include:

#### **Phase 1: Global Sourcing Tools**

* **💱 Multi-Currency Toggle:** Real-time switching between GBP (£), USD ($), and CNY (¥) to compare international supplier quotes instantly.
* **🚢 Freight Logic:** A "Landed Cost Calculator" adding Sea vs. Air freight estimates to the unit price for true cost comparison.

#### **Phase 2: Management Reporting**

* **📄 PDF Export Engine:** One-click generation of "Sourcing Approval Reports." Engineers can download a branded PDF with the break-even graph to attach to Purchase Requisitions (PRs).
* **💾 Local Storage:** Save specific scenarios (e.g., *"Slit Lamp Base Housing - Q3"*) to revisit later without re-entering data.

#### **Phase 3: Integration**

* **🔗 ERP Connector:** Potential for API integration to pull live Annual Demand figures directly from the ERP system, eliminating manual data entry.
* **📉 Supplier Scorecards:** Weighted scoring module to compare suppliers not just on price, but on Lead Time, Quality (PPM), and Risk.

---

### 🛠️ Technical Stack

* **Core:** HTML5, CSS3, Vanilla JavaScript (Zero dependencies, runs offline).
* **Visualization Engine:** Plotly.js for high-precision interactive charting.
* **Design System:** "Clinical" Theme – Clean, medical-grade UI with high contrast for readability.
* **Deployment:** Static Web App (Netlify/Vercel compatible) or local Intranet hosting.

---

### 🚀 Quick Start Guide

1. **Open the Tool:** Launch `index.html` in any modern browser (Chrome, Edge, Safari).
2. **Select Module:** Use the tabs to switch between *Make vs. Buy* and *Inventory Optimizer*.
3. **Input Data:**
    * *Make vs. Buy:* Enter Fixed Setup Costs (Tooling/NRE) and Variable Unit Costs.
    * *EOQ:* Enter Annual Demand, Unit Price, and Holding Cost %.
4. **Analyze:** The charts update instantly. Hover over lines to see exact cost/quantity data points.

---

### 📄 License

**Proprietary Software** tailored for internal procurement use.
*Concept & Development by James Gilbert.*
