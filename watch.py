import time
import shutil
from pathlib import Path
from config import REPO_BASE_DIR, README_HUB_DIR, SCAN_INTERVAL

def get_source_repo_dirs():
    """Scans the source domain and returns a set of valid repository directory names."""
    try:
        return {
            path.name for path in REPO_BASE_DIR.iterdir()
            if path.is_dir() and path.resolve() != README_HUB_DIR.resolve()
        }
    except FileNotFoundError:
        print(f"❌ ERROR: The domain at '{REPO_BASE_DIR}' could not be found.")
        return set()

def get_hub_repo_dirs():
    """Scans the Hub and returns a set of repository directory names it contains."""
    if not README_HUB_DIR.is_dir():
        return set()
    return {path.name for path in README_HUB_DIR.iterdir() if path.is_dir()}

def perform_sync_ritual(repo_name):
    """Copies or updates the README.md if the source is newer than the destination."""
    source_readme = REPO_BASE_DIR / repo_name / "README.md"
    if not source_readme.is_file():
        return  # Silently skip if no README exists

    target_dir = README_HUB_DIR / repo_name
    target_readme = target_dir / f"{repo_name}_README.md"

    should_copy = False
    action_message = ""

    if not target_readme.exists():
        should_copy = True
        action_message = f"📥 Copied new README for '{repo_name}'"
    else:
        source_mtime = source_readme.stat().st_mtime
        target_mtime = target_readme.stat().st_mtime
        if source_mtime > target_mtime:
            should_copy = True
            action_message = f"🔄 Updated README for '{repo_name}'"

    if should_copy:
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_readme, target_readme)
        print(action_message)

def begin_full_synchronization():
    """Continuously scans, syncing new, updated, and deleted repositories."""
    while True:
        print(f"\n--- Beginning sync cycle... (Next cycle in {SCAN_INTERVAL}s) ---")
        # The Custodian performs two surveys to compare reality with the archive.
        source_repos = get_source_repo_dirs() # What currently exists.
        hub_repos = get_hub_repo_dirs()      # What is currently archived.

        # --- Sync: Add and Update ---
        print(f"🔎 Checking {len(source_repos)} source repositories for updates...")
        for repo in source_repos:
            perform_sync_ritual(repo)

        # --- Sync: Prune and Clean (The Custodian's core duty) ---
        # By finding the difference, we identify what's in the Hub but no longer in the source.
        deleted_repos = hub_repos - source_repos
        if deleted_repos:
            print(f"🧹 Found {len(deleted_repos)} deleted repositories. Pruning from Hub...")
            for repo_name in deleted_repos:
                # The cleansing rite: remove the entire directory for the deleted repo.
                shutil.rmtree(README_HUB_DIR / repo_name)
                print(f"🗑️ Removed '{repo_name}' from Hub.")

        print("✅ Sync cycle complete.")
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    print("🧹 Awakening the Custodian...")
    README_HUB_DIR.mkdir(exist_ok=True)
    try:
        begin_full_synchronization()
    except KeyboardInterrupt:
        print("\n🛑 The Custodian's watch has ended. Goodbye!")
