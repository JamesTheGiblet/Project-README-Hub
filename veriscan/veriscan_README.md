# VeriScan - File Integrity Monitoring Solution

[![Go Version](https://img.shields.io/badge/go-1.21+-00ADD8.svg)](https://golang.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**VeriScan** is a comprehensive, high-performance File Integrity Monitoring (FIM) solution written in Go. It provides a powerful CLI, a full-featured REST API, and a real-time web dashboard to help you establish baselines, monitor for changes, and report on the integrity of your file systems.

## Features

### Core Engine

- **High-Performance Scanning**: Utilizes a concurrent worker pool for fast, parallel file hashing.
- **Flexible Hashing**: Supports multiple algorithms (`sha256`, `sha512`, `sha1`) via a centralized crypto package.
- **Partial Hashing**: Efficiently handles very large files by hashing samples from the beginning, middle, and end.
- **Robust Database**: Uses SQLite with performance optimizations (`WAL` mode) to store scan baselines, file hashes, and event logs.

### Command-Line Interface (CLI)

- `veriscan init`: Quickly sets up the default configuration and database.
- `veriscan scan <path>`: Creates a new file integrity baseline for a given directory.
- `veriscan watch`: Starts the real-time file system monitor.
- `veriscan diff`: Compares two scans and generates a detailed difference report.

### REST API

- Full-featured API to programmatically manage scans, monitor status, and generate reports.
- Endpoints for system health, statistics, and configuration management.
- Built with `gorilla/mux` and includes CORS support for web frontends.

### Web Dashboard

- **Real-time Overview**: A dashboard showing key stats like total scans, files tracked, and events.
- **Live Monitoring**: A dedicated page to view live file system events as they happen via WebSockets.
- **Scan Management**: Browse scan history, view detailed results, and compare baselines.
- **Reporting Interface**: Generate and view reports directly from the web UI.

### Advanced Reporting

- Generate detailed reports in multiple formats: **HTML**, **JSON**, **CSV**, and **Text**.
- Specialized reports like **Compliance** and **Executive Summaries**.

## Architecture

```text

veriscan/
├── cmd/veriscan/          # CLI entry point
├── internal/              # Internal application logic
│   ├── config/
│   ├── crypto/
│   ├── database/
│   ├── monitor/
│   ├── reporter/
│   └── scanner/
├── pkg/                   # Shared libraries (models, utils)
│   ├── models/
│   └── utils/
├── web/                   # Web interfaces
│   ├── api/               # REST API server
│   └── dashboard/         # Web Dashboard server
├── config.json            # Main configuration file
└── veriscan.db            # SQLite database
```

## Getting Started

### Prerequisites

- Go 1.21 or later

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/veriscan.git
    cd veriscan
    ```

2. Build the CLI tool:

    ```bash
    go build -o veriscan.exe ./cmd/veriscan
    ```

### Initialization

Before first use, initialize the configuration and database.

```bash
./veriscan.exe init
```

> **Note for Windows Users:** If you are using PowerShell, you must prefix the command with `.\` to run an executable from the current directory (e.g., `.\veriscan.exe init`). This is a security feature of PowerShell.
