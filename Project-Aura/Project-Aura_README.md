# 🌌 Aura: An Epistemic Trading Engine

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/yourusername/aura/workflows/CI/badge.svg)](https://github.com/yourusername/aura/actions)
[![codecov](https://codecov.io/gh/yourusername/aura/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/aura)

**Aura is not just a trading bot—it's a cognitive laboratory.**

Built on the Coinbase API, Aura transforms market interaction into a training ground for epistemic resilience. It synthesizes conflicting signals, quantifies uncertainty, and pits strategies against each other in dialectic tournaments. Every trade becomes a test of cognitive robustness.

---

## 🧠 Core Philosophy

Aura is founded on three interlocking principles:

### 1. 🔄 Contradiction as Signal

Conflicting indicators aren't noise—they're epistemic gold. Aura's **Contradiction Mapping Layer** quantifies signal coherence to measure uncertainty. When contradiction spikes, strategies adapt, pause, or recalibrate.

### 2. ⚔️ Dialectic Tournaments  

Strategies compete in simulated market stressors—like regime shifts and contradiction storms—to test adaptability, not just profitability. Aura's **Tournament Engine** fosters evolutionary pressure for superior cognitive design.

### 3. 🧬 Cognitive Archetypes

Each strategy is a cognitive persona—like **Volatility Sculptor** or **Contradiction Cartographer**—with unique strengths, biases, and learning goals. Contributors build strategies as archetypes, enriching Aura's epistemic ecosystem.

---

## ⚙️ Key Features

| Feature | Description |
|---------|-------------|
| 🧭 **Meta-Strategy Engine** | Classifies market regimes (trending, ranging, chaotic) using ADX and volatility metrics |
| 🤖 **Adaptive Execution** | Dynamically selects optimal strategy for current regime |
| 🎯 **Contradiction Mapping** | Quantifies signal conflicts and adjusts position sizing accordingly |
| 🏟️ **Dialectic Tournaments** | Pit strategies against epistemic challenges and stress tests |
| 📣 **Epistemic Notifications** | Narrative-rich alerts explain the "why" behind signals, including bias warnings |
| 🎓 **Cognitive Training Protocols** | Modules to train skills like Uncertainty Calibration and Narrative Flexibility |
| 🧬 **Archetype Framework** | Contributor system organized around cognitive trading personas |

---

## 🚀 Quick Start

### 🔧 Prerequisites

- Python 3.8+
- Coinbase Advanced Trade API credentials
- Basic understanding of technical analysis

### 📥 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/aura.git
cd aura

# Create and activate a virtual environment
# On Windows (PowerShell):
# python -m venv venv
# .\venv\Scripts\Activate.ps1
#
# On macOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# Install the project and its core dependencies
pip install -e .

# For contributing, install development and analysis tools (optional)
pip install -r requirements-dev.txt
```

### 🛠️ Configuration (for Live Data)

To run the bot with live data, you must configure your API credentials:

1. Rename the `.env.example` file in the root directory to `.env`.
2. Open the `.env` file and replace the placeholder text with your actual Coinbase API key and secret.

> **Security Note:**  
> The `.env` file is listed in `.gitignore`, so your secrets will never be committed to the repository.

Example `.env` file:

```env
COINBASE_API_KEY="your_actual_api_key"
COINBASE_API_SECRET="your_actual_api_secret"
```

### 📊 Basic Usage

To start the bot in its default paper trading mode, run the following command.
> **Note:** The `--mode` flag defaults to `paper` for safety.

```bash
aura trade --mode paper
```

Other useful commands:

```bash
# Run a one-off contradiction analysis with mock data
+aura contradiction --pair ETH-USD

# Run contradiction analysis with live data from Coinbase
+aura contradiction --pair BTC-USD --live

# Run a full tournament simulation using a high-level script
python scripts/run_tournament.py --type CONTRADICTION_STORM

---

## 🧬 Contributing Strategies
-
-Aura thrives on cognitive diversity. Choose your archetype and contribute!
-
### 🎭 Available Archetypes
-
-| Archetype | Focus | Cognitive Style |
-|-----------|-------|-----------------|
-| 🌊 **Volatility Sculptor** | Breakouts, regime changes | Pattern recognition, geometric intuition |
-| 🧭 **Momentum Mapper** | Trend following, momentum | Directional thinking, trend persistence |
-| ⚖️ **Contradiction Cartographer** | Signal conflicts, uncertainty | Synthesis thinking, ambiguity tolerance |  
-| 💭 **Sentiment Synthesizer** | Social signals, narratives | Empathy, crowd psychology |
-| 🔄 **Mean Reversion Artist** | Oscillators, extremes | Contrarian thinking, patience |
-
### 📝 Strategy Submission Process
-
-1. **Choose Your Archetype**: Select the cognitive persona that matches your trading philosophy
-2. **Create Strategy Manifest**: Define your approach using our YAML schema
-3. **Implement Strategy Logic**: Code your entry/exit conditions and risk management
-4. **Submit for Tournament**: Your strategy enters a mini-tournament for validation
-5. **Community Review**: Fellow contributors provide feedback and suggestions
+## 🧬 Contributing
+
+Aura thrives on cognitive diversity. We welcome contributions of all kinds, from new strategy archetypes to improvements in the core engines.
+
+Please see our [**CONTRIBUTING.md**](CONTRIBUTING.md) file for detailed guidelines on how to participate, choose your cognitive archetype, and submit your work for review.

-```bash
# Validate your strategy
-./aura validate --manifest manifests/your_strategy.yaml
-
# Submit for review
-./aura submit --strategy your_strategy --archetype volatility_sculptor
-```
-
### 🏅 Epistemic Badges
-
-Contributors earn badges for cognitive achievements:
-
-- 🎯 **Uncertainty Navigator**: Excellence in low-coherence environments
-- 🔄 **Contradiction Synthesizer**: Superior conflict resolution
-- 📡 **Regime Detector**: Early identification of market shifts
-- 📖 **Narrative Architect**: Compelling market storytelling
-- ⚖️ **Risk Sculptor**: Exceptional risk/reward optimization
-
---

## 🏟️ Dialectic Tournaments

Tournaments test strategies beyond simple profit metrics:

### Tournament Types

| Tournament | Challenge | Tests |
|------------|-----------|-------|
| **Regime Shift** | Sudden market transitions | Adaptability, meta-cognition |
| **Contradiction Storm** | High signal conflict periods | Uncertainty handling, synthesis |
| **Black Swan** | Extreme market events | Risk management, resilience |
| **Whipsaw** | Rapid oscillations | Emotional regulation, patience |
| **Narrative Collapse** | Story breakdown events | Flexibility, belief updating |

### Scoring Metrics

- **Returns**: Traditional profit/loss
- **Epistemic Score**: Adaptability and learning
- **Coherence Handling**: Performance during uncertainty
- **Risk Management**: Drawdown control and position sizing
- **Cognitive Growth**: Improvement over time

---

## 📚 Documentation

- [📖 Getting Started Guide](docs/getting-started.md)
- [🧠 Cognitive Archetypes](docs/cognitive-archetypes.md)
- [⚔️ Dialectic Tournaments](docs/dialectic-tournaments.md)
- [🔄 Contradiction Mapping](docs/contradiction-mapping.md)
- [🛠️ API Reference](docs/api-reference.md)
- [📊 Example Notebooks](notebooks/)

---

## 🗺️ Roadmap

| Version | Highlights | Status |
|---------|------------|---------|
| **v1.0** | Contradiction Mapper, Regime Classifier, Tournament Engine | 🚧 In Progress |
| **v1.1** | Contributor Framework, Archetype Manifests | 📋 Planned |
| **v1.2** | Cognitive Training Protocols, Replay Engine | 💭 Conceptual |
| **v2.0** | Live Trading, Advanced Risk Management, Multi-Exchange | 🔮 Future |

---

## 🤝 Community

- **Discord**: [Join our cognitive trading community](https://discord.gg/aura-trading)
- **Twitter**: [@AuraTrading](https://twitter.com/auratrading)
- **Blog**: [Epistemic Trading Insights](https://blog.auratrading.dev)

---

## ⚖️ Risk Disclaimer

**Aura is experimental software designed for educational and research purposes.**

- Cryptocurrency trading carries significant financial risk
- Past performance does not guarantee future results  
- Use paper trading mode before risking real capital
- Only trade with money you can afford to lose
- Aura's cognitive training focus does not guarantee profitable trades

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Coinbase** for their robust API infrastructure
- **The Behavioral Economics Community** for insights into cognitive biases
- **Open Source Contributors** who make projects like this possible
- **The Trading Psychology Research Community** for foundational work

---

## 🧭 Join the Cognitive Tournament

Aura isn't just code—it's a dialectic. Every strategy is a hypothesis. Every contradiction is a lesson. Every contributor is a cognitive architect.

**Ready to trade uncertainty?**

[🚀 Get Started](docs/getting-started.md) | [🧬 Contribute](CONTRIBUTING.md) | [⚔️ Enter Tournament](docs/dialectic-tournaments.md)

---

### Built with 🧠 by the Aura Community

*"In the contradiction lies the hope."* — Bertolt Brecht
