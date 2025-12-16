# **The README Hub** 🛠️

Stop navigating. Start knowing. A simple, powerful tool to centralize all your project READMEs.

-----

## **The Problem**

As a developer, you're always jumping between projects. Remembering the setup, purpose, or status of each one means constantly changing directories. It's a waste of time and mental energy. This tool was built to fix my own problem.

### **How It Works**

It scans your project folder, finds all the `README.md` files, and dumps them into a single, organized "hub" directory. It can run once to build the hub, or run continuously to keep it perfectly in sync.

-----

### **Features**

* **Automatic Discovery:** Scans your project directory and finds all repositories automatically.
* **Simple CLI:** Just a simple command line interface to control it.
* **Three Modes:**
  * `survey`: A "dry run" to see what projects will be included.
  * `archive`: A one-time sync to build or update the hub.
  * `watch`: A "set-it-and-forget-it" mode that watches your projects and keeps the hub up to date.
* **Zero-Dependency:** Runs on a standard Python installation. No `pip install` needed. You don't even have to mess with a virtual environment.
* **Clean & Organized:** Creates a dedicated sub-folder in the hub for each project, with a clearly named README file (`[repo_name]/[repo_name]_README.md`).

-----

### **Getting Started**

1. **Clone the repo.**

2. **Configure:** Open `config.py` and set the `REPO_BASE_DIR` to your main projects folder.

    ```python
    # config.py
    from pathlib import Path

    REPO_BASE_DIR = Path(r"C:\Path\to\your\Projects")
    README_HUB_DIR = Path(r"C:\Path\to\your\Projects\Project-README-Hub")
    ```

3. **Run it:** Use the `hub_manager.py` script from your terminal.

### **Commands**

-----

### `survey`

Does a "dry run" to see what will be found without copying anything.

```bash
python hub_manager.py survey
```

### `archive`

A one-time sync to build or update the hub.

```bash
python hub_manager.py archive
```

### `watch`

Starts the continuous monitor to keep the hub perfectly synchronized. This is the "set it and forget it" mode. Press `Ctrl+C` to stop.

```bash
python hub_manager.py watch
```

-----

### **Project Structure**

* `hub_manager.py`: The main entry point and command-line interface.
* `core.py`: Contains all the core logic for scanning and syncing files.
* `config.py`: Centralized configuration for all paths and settings.

The other individual scripts (`archivist.py`, `custodian.py`, etc.) are historical artifacts from the development process and are no longer used. I left them in so you can see the mess that came before this final working blueprint. The code is a proof of the process.

-----
