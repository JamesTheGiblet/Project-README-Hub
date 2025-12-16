# ⚡ Emergent Stock Monitor

A sophisticated, single-page web application for real-time stock market monitoring. This tool goes beyond traditional watchlists by visualizing market data as a dynamic, emergent system, revealing hidden patterns and trends through a physics-based particle simulation.

![Emergent Stock Monitor Screenshot](https://via.placeholder.com/800x500.png?text=Emergent+Stock+Monitor+UI)

***

## ✨ Features

The Emergent Stock Monitor is packed with features designed for both at-a-glance insights and deep analysis.

### Watchlist Management

- **Add & Remove Stocks**: Easily add stocks by their ticker symbol (e.g., `NVDA`, `GOOGL`) and remove them from the detail view.
- **Persistent Watchlist**: Your watchlist is automatically saved to your browser's local storage.
- **Drag-and-Drop Reordering**: In the "Detailed" view, simply drag stocks to reorder your list.
- **Group by Sector**: Toggle grouping to organize your watchlist by industry sector for a clearer overview.

### Multiple Viewing Modes

- **Compact View**: A high-level dashboard with large, color-coded cards showing the symbol, price, and daily change. Perfect for a quick market pulse check.
- **Detailed View**: A more traditional list format that provides additional data like stock name, volume, and sector. This view also enables reordering.
- **Emergent View**: The core of the application. It visualizes your watchlist as a system of interacting particles, where you can observe market dynamics unfold in real-time.

### In-Depth Stock Analysis

- **Interactive Modal**: Click on any stock to open a detailed modal.
- **Multiple Chart Types**: Visualize historical data with either a **Line Chart** (with area gradient) or a professional **Candlestick Chart**. You can toggle between them instantly.
- **Dynamic Chart Updates**: If the modal is open during a data refresh, the chart will automatically update with the latest price point.
- **Technical Indicators**: Get key metrics at a glance, including:
  - **RSI (Relative Strength Index)**: To identify overbought or oversold conditions.
  - **MACD (Moving Average Convergence Divergence)**: To gauge trend momentum.
- **AI-Powered Prediction**: A simple linear regression model predicts the next day's price trend (upward/downward) and potential percentage change, with a calculated confidence score.

### The Emergent System

- **Particle Simulation**: Each stock is a particle whose size is based on its trading volume. Particles with positive daily changes glow green, while negative ones glow red.
- **Behavioral Rules**: Particles interact based on simple rules:
  - **Attraction**: Stocks with the same sentiment (both positive or both negative) pull towards each other.
  - **Repulsion**: Particles maintain a minimum distance to avoid overlap.
  - **Alignment**: Stocks within the same sector tend to move together as a flock.
- **Particle Simulation**: Each stock is a particle whose size is based on its trading volume. Particles with positive daily changes glow green, while negative ones glow red.
- **Behavioral Rules**: Particles interact based on simple rules:
  - **Attraction**: Stocks with the same sentiment (both positive or both negative) pull towards each other.
  - **Repulsion**: Particles maintain a minimum distance to avoid overlap.
  - **Alignment**: Stocks within the same sector tend to move together as a flock.
- **Pattern Detection**: The system automatically identifies and alerts you to emergent patterns, such as:
  - **Momentum Clusters**: Groups of stocks moving strongly in the same direction.
  - **Sector Movement**: Coordinated movement within a specific industry sector.
  - **Volume Anomalies**: Stocks experiencing unusually high trading volume.
- **Market Pulse**: A dashboard widget that summarizes the overall market's **Momentum** and **Volatility**, classifying the current state (e.g., `BULL EMERGENCE`, `BEAR EMERGENCE`, `CHAOS`).

### Data & Performance

- **Real-Time Data**: Stock prices are fetched from the Yahoo Finance API and updated automatically.
- **Performance Optimized**: The particle system uses a spatial grid to efficiently calculate interactions, ensuring smooth animation even with many stocks.
- **Data Export**: Export data for a single stock or your entire watchlist to a JSON file.

### Customization & Control

- **Advanced Settings Panel**: Take full control of the application with a dedicated settings panel.
  - **API Key Management**: Enter your own `corsproxy.io` API key.
  - **Custom Refresh Rate**: Set the data refresh interval to your preferred frequency (in seconds).
  - **Tunable Technical Indicators**: Adjust the parameters for RSI (period) and MACD (fast, slow, signal) to match your trading strategy.
  - **Reset to Defaults**: Easily revert all settings back to their original state.

### Accessibility & UX

- **Responsive Design**: A clean, modern UI that works seamlessly on desktop and mobile devices.
- **Robust Error Handling**: User-friendly notifications for API failures or invalid inputs.
- **Accessible**: Built with ARIA roles, proper keyboard navigation, and high-contrast colors for readability.

***

## 🚀 Getting Started

This is a single-file web application with no build process required.

1. **Download the File**: Save the `emergent-stock-monitor.html` file to your local machine.
2. **Open in Browser**: Open the HTML file directly in a modern web browser like Chrome, Firefox, or Edge.

That's it! The application will load with a default set of stocks. You can start adding your own right away.

***

## 💡 How to Use

1. **Add a Stock**: Type a stock symbol (e.g., `TSLA`) into the search bar at the top and click "Add".
2. **Switch Views**: Use the "Compact", "Detailed", and "Emergent" buttons to switch between layouts.
3. **View Details**: Click on any stock card in any view to open the detailed analysis modal.
4. **Organize Your Watchlist**:
    - In the "Detailed" view, **click and drag** a stock card to change its position.
    - Click the **"Group by Sector"** button to toggle grouping.
5. **Remove a Stock**: Open the detail modal for the stock you want to remove and click the "Remove Stock" button.
6. **Export Data**: Use the "Export Data" button in the header or the "Export This Stock" button in the modal.
7. **Customize Settings**: Click the **gear icon (⚙️)** in the header to open the settings panel and adjust API keys, refresh rates, and indicator parameters.

***

## 🔬 The Emergent View Explained

The "Emergent View" is what makes this tool unique. It's based on the concept of **emergence**, where complex patterns arise from simple interactions.

Instead of just looking at a list of numbers, this view allows you to *see* the market's behavior. Are all tech stocks moving together? Is there a cluster of high-momentum stocks forming? Is the market calm or chaotic? These are the kinds of insights that become immediately visible in the emergent simulation.

The **Pattern Alerts** and **Market Pulse** widgets provide a structured interpretation of the complex simulation, giving you actionable insights derived from the system's behavior.

***

## 🛠️ Technology Stack

- **Frontend**:
  - **HTML5**: For the application structure and semantics.
  - **CSS3**: For styling, animations, and responsive design (utilizing Flexbox, Grid, and CSS Variables).
  - **JavaScript (ES6+)**: For all application logic, including API calls, DOM manipulation, and the physics simulation.

- **APIs & Data**:
  - **Yahoo Finance API**: Used as the source for all stock quote and historical data.
  - **CORS Proxy**: A proxy is used to bypass Cross-Origin Resource Sharing (CORS) restrictions when fetching data from the API in a browser environment.

- **Libraries**:
  - **None!** This project is built with vanilla JavaScript to remain lightweight and demonstrate core principles.

***

## 📜 License

This project is open-source and available for personal and educational use. Please see the `LICENSE` file for more details.
