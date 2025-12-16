# ORLIN Motion Sizing Engine

## 🚀 Professional Motion Control Calculator for Engineers

**ORLIN Motion Sizing Engine** is an advanced web-based motion profile calculator designed for mechanical engineers, motion control specialists, and automation professionals. This tool provides precise calculations for linear motion systems with an intuitive interface that combines engineering accuracy with practical usability.

### 🌟 Key Features

#### **1. Dynamic Velocity Profile Visualization**

- Real-time plotting of trapezoidal vs. triangular motion profiles
- Interactive chart with fill-to-zero area for clear acceleration/deceleration visualization
- Instant updates as parameters change

#### **2. Comprehensive Motion Parameter Control**

- **Total Stroke**: 1-200 mm precision control
- **Move Time**: 20-1000 ms range with 10 ms steps
- **Moving Mass**: 10-2000 g capacity
- **Profile Selection**: Toggle between trapezoidal (standard) and triangular (high-speed) profiles

#### **3. Environmental Factor Modeling**

Six predefined environmental factors that modify calculations:

- **Vertical Mount**: Adds gravitational force (9.81 m/s²)
- **High Friction**: Simulates rail friction (μ = 0.2)
- **Air Bearing**: Models near-zero friction environments (μ = -0.05)
- **Safety Factor**: Applies 50% design headroom (1.5x multiplier)
- **Return Spring**: Accounts for additional 2N force
- **Vacuum Load**: Simulates hose drag (0.5 g mass addition)

#### **4. Professional Output Metrics**

Four critical engineering parameters calculated in real-time:

- **Peak Force (N)**: Maximum required actuator force
- **Acceleration (G)**: Motion profile acceleration in G-forces
- **Peak Velocity (m/s)**: Maximum velocity during movement
- **Holding Force (N)**: Static force requirements

#### **5. Intelligent System Recommendations**

AI-style recommendations based on calculated requirements:

- **Extreme Dynamics**: Warns when >10G acceleration requires specialized moving coil technology
- **High Performance**: Recommends appropriate actuator types for 5-10G applications
- **Micro-Positioning**: Suggests piezo flexure or voice coil for short-stroke, fast moves
- **Standard Applications**: Identifies compatible linear stages for typical requirements

### 🎯 Use Cases

#### **Industrial Automation**

- Sizing linear actuators for pick-and-place machines
- Calculating motor requirements for automated assembly lines
- Determining force needs for robotic positioning systems

#### **Precision Engineering**

- Micro-positioning stage design
- Laboratory automation equipment
- Semiconductor manufacturing tools

#### **Research & Development**

- Prototype motion system sizing
- Educational tool for motion control principles
- Comparative analysis of different motion profiles

### 🔧 Technical Implementation

#### **Physics Model**

The calculator uses fundamental motion equations:

**For Triangular Profile:**

```txt
v_peak = (2 * distance) / time
acceleration = v_peak / (time / 2)
```

**For Trapezoidal Profile:**

```txt
v_peak = 1.5 * (distance / time)
acceleration = v_peak / (time / 3)
```

**Total Force Calculation:**

```txt
F_total = (F_accel + F_gravity + F_friction + F_extra) × Safety_Factor
```

#### **Technology Stack**

- **Frontend**: Pure HTML5, CSS3, JavaScript (no frameworks)
- **Visualization**: Plotly.js for high-performance charting
- **Icons**: Font Awesome 6.4.0
- **Styling**: Custom CSS with engineering-inspired design system
- **Responsive Design**: Mobile-first approach with precision grid layout

### 📊 Engineering Features

#### **Dynamic Duty Cycle Indicator**

- Visual load percentage bar with color coding:
  - **Green** (<50%): Safe operating range
  - **Orange** (50-80%): High performance zone
  - **Red** (>80%): Requires specialized components
- Real-time capacity percentage calculation

#### **Active Constraint Management**

- Visual stack of applied environmental factors
- One-click reset functionality
- Interactive toggle selection with visual feedback

#### **Three-Tab Interface**

1. **Profile Tab**: Motion visualization and parameter control
2. **Conditions Tab**: Environmental factor application
3. **Datasheet Tab**: Calculated results and recommendations

### 🎨 Design Philosophy

#### **ORLIN Corporate Theme**

- Professional color scheme: Deep blue (#003B73) with tech orange (#FF6B00)
- Engineering grid background (20px × 20px)
- Sharp, precise corners (4px radius) for technical appearance
- Clear typography hierarchy with uppercase headings

#### **UI Components**

- **Technical Datasheet Header**: Sticky navigation with brand identity
- **Toggle-Style Tabs**: Engineering panel navigation
- **Precision Inputs**: Slider controls with numeric readouts
- **Digital Readout Panels**: Monospace fonts for technical values
- **Interactive Item Cards**: Icon-based factor selection

### 🚀 Getting Started

#### **Quick Start**

1. Open `index.html` in any modern browser
2. Adjust stroke, time, and mass parameters in the Profile tab
3. Select environmental factors in the Conditions tab
4. View calculated requirements and recommendations in the Datasheet tab

#### **Usage Tips**

1. **For High-Speed Applications**: Enable triangular profile for fastest move times
2. **Vertical Mounting**: Always add the Vertical Mount factor for gravity compensation
3. **Safety Margin**: Apply Safety Factor for real-world applications
4. **System Matching**: Use the duty cycle indicator to select appropriately sized actuators

### 📈 Performance Specifications

#### **Calculation Ranges**

- **Distance**: 1-200 mm (0.001-0.2 m)
- **Time**: 20-1000 ms (0.02-1.0 s)
- **Mass**: 10-2000 g (0.01-2.0 kg)
- **Force Output**: 0-100+ N (theoretical maximum)
- **Acceleration**: 0-100+ G (theoretical maximum)

#### **Environmental Factor Effects**

- **Friction Range**: -0.05 to 0.2 coefficient
- **Safety Factors**: 1.0-1.5x multiplier
- **Additional Forces**: ±0-10 N range
- **Mass Modifications**: ±0-500 g adjustments

### 🔍 Technical Details

#### **Algorithm Accuracy**

- 64-bit floating point calculations
- Real-time physics simulation
- Unit conversion (mm→m, ms→s, g→kg) with 6 decimal precision
- Dynamic scaling for visualization

#### **Browser Compatibility**

- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+
- Mobile Safari/Chrome on iOS/Android

### 🏭 Industry Applications

#### **Manufacturing**

- Conveyor system design
- CNC machine component sizing
- Packaging machine actuator selection

#### **Medical Devices**

- Laboratory automation
- Diagnostic equipment positioning
- Surgical robot arm sizing

#### **Aerospace & Defense**

- Gimbaled platform design
- Antenna positioning systems
- Testing equipment motion control

### 📚 Educational Value

This tool demonstrates fundamental principles of:

- Kinematics and dynamics
- Motion profile optimization
- Force and acceleration calculations
- System design with safety margins
- Environmental factor considerations

### 🔗 Integration Potential

The modular JavaScript architecture allows for:

- **API Integration**: Connect with motor database APIs
- **Export Functions**: Add CSV/PDF report generation
- **Cloud Sync**: Save and share configurations
- **Team Collaboration**: Multi-user scenario comparison

### 🛠️ Development Roadmap

#### **Planned Features**

1. **Motor Database Integration**: Direct component recommendations
2. **Energy Consumption Calculator**: Power requirements and efficiency
3. **Advanced Profiles**: S-curve and custom motion profiles
4. **3D Visualization**: Animated motion simulation
5. **Export Reports**: Professional PDF datasheet generation
6. **Multi-Axis Calculations**: Coordinated motion systems

### 📄 License & Usage

**Internal Use**: Free for engineering teams and educational purposes
**Commercial Use**: Contact ORLIN Engineering for licensing

### 👥 Contributing

This project welcomes:

- Bug reports and feature requests
- Documentation improvements
- Physics model enhancements
- UI/UX design contributions

---

**Motion Sizing Engine** – Precision in Motion, Engineered for Professionals.

#### Version 2.4 PRO | Last Updated: 2025
