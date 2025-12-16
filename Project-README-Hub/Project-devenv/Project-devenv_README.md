# ⚡ devenv

Reproducible dev environments in **2 seconds**.  
No Docker. No VMs. No cloud lock-in.

*Local-first development environments. Cloud speed, laptop reliability.* \> "Your laptop is the only computer you can trust. Everything else is just distributed disappointment."

-----

## 🚀 Quick Start

# Install
curl -fsSL https://devenv.sh/install.sh | sh

# Create environment
devenv create node@20 postgres@15 redis@7

# Enter
devenv shell

✅ That’s it. Dependencies, services, and runtime are up in seconds.
No Dockerfile, no Compose, no YAML.
Just code. (And your sanity.)

---

🌍 Share Instantly

# Export your environment
devenv share blog > blog.devenv

# Teammate runs:
devenv import blog.devenv

Everyone gets the same runtime, same services, same dependencies.
No docs. No setup. Just code.

---

⚡ Why devenv?

Modern dev environments are broken:

Docker: 🐌 slow, heavy, eats RAM

Nix: ❄️ powerful, but complex

Cloud IDEs: ☁️ expensive, laggy, dependent on someone else’s server


devenv is different:

Traditional Dev Setup:
[VM] → [Daemon] → [Image] → [Container] → [Your App]

devenv:
[devenv create] → [Your App]

Cold start: 10–15s (vs minutes)

Warm start: 2s (vs 30–60s)

RAM usage: 50–100MB (vs 1–4GB)

Cost: $0 (vs $50–200/mo cloud IDEs)

---

📊 Comparison

Metric	devenv ⚡	Docker 🐳	Nix ❄️	Cloud IDE ☁️

Cold start	10-15s	60-120s	30-45s	60-180s
Warm start	2s	15-30s	10-15s	30-60s
RAM usage	50-100MB	1-4GB	200-500MB	❌
Offline work	✅	⚠️ Limited	✅	❌
Native speed	✅	❌	✅	⚠️
Monthly cost	$0	$5-21	$0	$50-200

---

🛡️ Secure by Default

No privileged daemons

No root inside your laptop

Process isolation via Rust + namespaces

Ephemeral by design → your system stays clean

---

🛠️ Features

🔥 Blazing fast → 2s warm boots

🧩 Modular → services, runtimes, tools snap in/out

🌍 Portable → share with a single file

🛡️ Safe → sandboxed, no leaks into host system

📴 Offline-ready → dev anywhere, plane mode approved

🏎️ Native speed → no VM overhead, no FS lag

---

📦 Supported Stacks

Node.js (14–22)

Python (3.8–3.13)

Go, Rust, Java

PostgreSQL, MySQL, Redis, MongoDB

Bun, Deno, Zig, Elixir, PHP, Ruby


…and more on the roadmap.

---

📥 Install

curl -fsSL https://devenv.sh/install.sh | sh

Supports Linux & macOS.
Windows (WSL2) support coming soon.

---

📚 Documentation

[Getting Started Guide](#)

[Command Reference](#)

[Service Catalog](#)

---

🤝 Get Involved

[⭐ Star on GitHub](https://github.com/devenv/devenv)

[💬 Join Discord](#)

[🐦 Follow on Twitter](#)

[📖 Docs](#)

---

🗺️ Roadmap

[x] Fast environments (done)

[x] Sharing (devenv share)

[ ] GUI dashboard

[ ] Windows/WSL support

[ ] GPU workloads (ML/AI ready)

[ ] VS Code + JetBrains integrations

---

📜 License

MIT. Free forever.

Before we move on, should we consider how the GUI dashboard and VS Code integration will be monetized?
```
