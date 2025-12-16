<div align="center">

# 🧬 ImperfectaForge

## Perfection from Imperfection

[![Language: HTML](https://img.shields.io/badge/Language-HTML-orange?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Language: CSS](https://img.shields.io/badge/Language-CSS-blue?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Language: JS](https://img.shields.io/badge/Language-JavaScript-yellow?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Tech: Vanilla JS](https://img.shields.io/badge/Tech-Vanilla_JS-yellowgreen?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Glossary/Vanilla_JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)

A simple, interactive, and dependency-free web-based simulation of a genetic algorithm. Watch as a target phrase is evolved from a parent of pure random nonsense.

</div>

---

## [➡️ View Live Demo](https://JamesTheGiblet.github.io/ImperfectaForge/ImperfectaForge.html) ⬅️ *(If published with GitHub Pages)*

Repository: [https://github.com/JamesTheGiblet/ImperfectaForge.git](https://github.com/JamesTheGiblet/ImperfectaForge.git)

![ImperfectaForge Screenshot](https://github.com/JamesTheGiblet/ImperfectaForge/raw/main/screenshot.png)
*(Replace with a screenshot or GIF of the application in action, e.g., screenshot.png in your repo)*

---

## 🎯 What is This?

ImperfectaForge is a tool that vividly demonstrates a **genetic algorithm** in action. The core idea is to show how a "perfect" target phrase can be evolved from a "parent" string of pure random nonsense.

Each generation, a population of "children" is created. Each child has a chance of a **random mutation (Imperfection)**. Only the *fittest* child—the one whose string is most similar to the target—is selected to become the new parent for the next generation **(Perfection)**. This cycle repeats, gradually "forging" the perfect phrase from imperfect beginnings.

## ⚙️ How It Works

The simulation follows a classic and simple genetic algorithm model:

1. **Initialization**: A target phrase is set. A random string of the same length is generated to be the first "Parent".
2. **Population Generation**: In each cycle (a "generation"), a new population of "children" is created. Each child is a copy of the current Parent.
3. **Mutation (Imperfection)**: For every character in each child's string, there is a small, random chance (the *Mutation Rate*) that it will be replaced with a random character from a defined character set.
4. **Fitness Calculation**: Each child is scored based on its "fitness"—how many of its characters match the target phrase's characters at the same position.
5. **Selection (Perfection)**: The single child with the highest fitness score from the entire population is selected.
6. **Evolution**: This "fittest child" becomes the new Parent for the next generation.
7. **Repeat**: The process repeats from Step 2. Over many generations, the Parent string evolves to perfectly match the Target string.

## ✨ Features

- **Real-time Evolution**: Watch the best string evolve character by character towards the target.
- **Interactive Controls**: **Start**, **Pause**, **Resume**, and **Step** through the evolution one generation at a time.
- **Live Statistics**:
  - **Generation**: Tracks the number of cycles.
  - **Fitness**: Shows the current score of the best string.
  - **Mutation Rate**: Displays the currently set mutation probability.
  - **Speed**: Measures the number of generations calculated per second.
- **Visual Fitness Graph**: A real-time graph plots the fitness of the best string over time, showing the march towards perfection.
- **Full Customization**:
  - **Target Phrase**: Set any target phrase you want.
  - **Population Size**: Control how many children are generated in each generation.
  - **Mutation Rate**: Adjust the mutation probability with a slider.
  - **Character Set**: Choose from pre-defined character sets (Alphanumeric, Letters, Numbers) or provide your own custom set.
- **Result Export**: Save the results of your simulation—including the final strings, stats, and fitness history—to a `.txt` file.
- **Responsive Design**: Works on both desktop and mobile browsers.
- **Zero Dependencies**: Written in pure, vanilla HTML, CSS, and JavaScript. No frameworks or libraries needed!

## 🚀 How to Use

Since this is a self-contained HTML file, getting started is incredibly simple.

1. **Download the File**:
    - Clone this repository: `git clone https://github.com/JamesTheGiblet/ImperfectaForge.git`
    - OR, simply download the `ImperfectaForge.html` file.
2. **Open in Browser**:
    - Open the `ImperfectaForge.html` file directly in your favorite web browser (like Chrome, Firefox, or Edge).

That's it! You can now run your own evolution simulations.

## 🔧 Customization Guide

1. **Enter Target Phrase**: Type your desired phrase into the main input box.
2. **Adjust Parameters**: Use the controls in the "Customization" panel to fine-tune the simulation.
    - A **higher population size** may find the solution faster but will be more computationally expensive (lower gen/s).
    - A **higher mutation rate** introduces more randomness. This can help escape a "local maximum" but may also slow down the final steps of perfection.
3. **Start Evolution**: Click the "Start Evolution" button and watch the process unfold.

## 📊 Example Export

Here is a sample export from a successful run of ImperfectaForge:

```txt
🧬 ImperfectaForge - Evolution Export
-------------------------------------
Date: Sat, 15 Nov 2025 13:22:20 GMT

Target (Perfection):
Out of simplicity, complexity is born.

Evolved (from Imperfection):
Out of simplicity, complexity is born.

Stats:
<!--
ImperfectaForge is part of the Forge Theory series. Learn more at:
👉 [Forge Theory](https://github.com/JamesTheGiblet/forge_theory)
-->
Character Set: alphanumeric

---

## 🧩 Background & Context

ImperfectaForge is inspired by the principle that <em>"out of simplicity, complexity is born."</em> It demonstrates how simple rules—mutation, selection, and inheritance—can give rise to sophisticated, emergent behavior. This project is a member of the <a href="https://github.com/JamesTheGiblet/forge_theory">Forge Theory</a> ecosystem, which includes simulations of life, language, art, economics, and more. Each Forge explores a different aspect of emergence, and ImperfectaForge focuses on the evolution of information through genetic algorithms.

**Why does this matter?**

- Shows how genetic algorithms work in a visual, hands-on way
- Makes abstract concepts like fitness landscapes and mutation rates tangible
- Serves as a learning tool for students, educators, and anyone curious about complexity science

## 🛠️ Technical Details

- **Stack:** Pure HTML, CSS, and JavaScript (no frameworks, no build step)
- **Performance:** Optimized for real-time updates and smooth animation
- **Portability:** Works offline, on any modern browser, desktop or mobile
- **Customization:** All parameters (target, mutation, population, charset) are user-adjustable
- **Export:** Results and fitness history can be saved as a `.txt` file for analysis or sharing
- **Accessibility:** Designed for clarity and ease of use, with responsive layout

---

## 🚧 Future Development & Roadmap

- **Parameter Presets:** Add one-click presets for famous phrases, numbers, or code snippets
- **Advanced Graphs:** Add more detailed visualizations (e.g., mutation distribution, population diversity)
- **Challenge Mode:** Timed or competitive evolution challenges
- **Multi-Target Evolution:** Evolve towards multiple targets or allow user-defined fitness functions
- **Mobile UI Enhancements:** Further optimize controls and layout for small screens
- **Accessibility:** Improve keyboard navigation and screen reader support
- **Integration:** Link results to the broader Forge Theory ecosystem (e.g., export to other Forges)
- **Localization:** Add support for multiple languages
- **Educational Content:** Built-in tutorials, tooltips, and links to further reading

<em>Have ideas or want to contribute? Open an issue or pull request!</em>
