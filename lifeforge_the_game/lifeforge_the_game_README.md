# 🧬 LifeForge: Developmental Biology Simulator

<p align="center">
  <strong>Watch life emerge from a single cell.</strong>
  <br />
  <em>A web-based game simulating the journey from a single cell to a complex, multi-cellular organism through the principles of developmental biology.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-playable_alpha-green.svg" alt="Project Status" />
  <img src="https://img.shields.io/badge/tech-html_&_js-blue.svg" alt="Technology" />
  <img src="https://img.shields.io/badge/license-mit-lightgrey.svg" alt="License" />
</p>

---

## 🚀 Current Project Status

LifeForge is currently a **feature-rich, playable alpha** built as a single-file web application. The core simulation engine is robust, and the project has moved beyond a basic prototype to include significant gamification, visualization, and user-interaction features.

The simulation is stable and includes performance optimizations (like a spatial grid for cell lookups) to handle thousands of cells. The focus has been on creating an engaging and educational experience that visually represents complex biological processes.

## ✨ Key Features

The simulation is packed with features to control, observe, and interact with your growing organism:

* **Cellular Simulation**: A core engine where cells live, consume energy, and die based on environmental conditions.
* **Division & Differentiation**: Stem cells divide and differentiate into specialized types (Neural, Muscle, Digestive, etc.) based on chemical gradients (morphogens).
* **Interactive Control Panel**:
  * Adjust **Development Speed**, **Mutation Rate**, and **Cell Division Rate**.
  * Modify **Environmental Factors** like Temperature, Toxicity, and Nutrient Levels to see how your organism adapts.
* **Gamification & Progression**:
  * **Challenge System**: Complete objectives like "Reach 10 cells" or "Survive a Toxin Storm" to earn rewards.
  * **Unlockable Cell Types**: Progress through challenges to unlock advanced cells like **Structural** and **Reproductive** types, granting new strategic possibilities.
  * **Predators**: Spawn predators to test your organism's resilience.
* **Advanced Visualization**:
  * **Multiple View Modes**: Switch between viewing Cell Types, Chemical Gradients, Energy Levels, and Gene Activity.
  * **Dynamic Chart**: A population chart tracks the count of each cell type over time.
  * **Particle System**: Rich visual effects for cell division, death, differentiation, and chemical signals.
* **User Experience**:
  * **Interactive Tutorial**: A step-by-step guide for new players.
  * **Pan & Zoom**: Freely navigate the canvas to inspect your organism up close.
  * **Cell Inspector**: Click on any cell to see its detailed stats, including type, age, and energy.
  * **Notifications & Achievements**: Get feedback on challenges, unlocks, and random events.

## 🎮 How to Play

1. **Open `lifeforce.html` in a modern web browser.**
2. (Optional) Click **"Start Tutorial"** for a guided introduction.
3. Click **"Start Development"** to begin the simulation.
4. Use the sliders in the **Control Panel** to influence how your organism grows.
5. Try to complete the objectives listed in the **Active Challenges** panel to unlock new features.
6. Use the **Interventions** buttons to introduce mutations, predators, or new cells and see what happens!

## 🔧 How It Works

The simulation is self-contained within a single HTML file, utilizing vanilla JavaScript and the Chart.js library.

* **`Cell` Class**: Manages the state and behavior of individual cells, including energy, age, and differentiation logic.
* **`MorphogenField` Class**: Simulates the production and diffusion of chemical signals that guide cell differentiation, creating emergent patterns.
* **`SpatialGrid` Class**: A critical performance optimization that provides fast, O(1) lookup of cells at any coordinate, preventing slowdowns as the organism grows.
* **Main Game Loop (`update`)**: The core `requestAnimationFrame` loop that processes cell updates, division, adhesion, and rendering for each frame.

## 🛣️ Future Roadmap

While the current version is comprehensive, here are some potential next steps:

* **More Complex Structures**: Implement logic for forming functional organs and systems (e.g., a nervous system that actually controls muscle cells).
* **Reproduction Cycle**: Fully implement the reproductive cells to allow organisms to create offspring that inherit traits.
* **Evolution & Genetics**: Introduce a simple genetic system where mutations are passed down, allowing for true evolution across generations.
* **Save/Load State**: Allow players to save their creations and continue their experiments later.

---

<p align="center">
  <em>LifeForge - Where information becomes form.</em>
</p>
