import shutil
from pathlib import Path
from config import REPO_BASE_DIR, README_HUB_DIR

def get_repo_dirs():
    """Scans the base directory and returns a set of valid repository directory names."""
    try:
        return {
            path.name for path in REPO_BASE_DIR.iterdir()
            if path.is_dir() and path.resolve() != README_HUB_DIR.resolve()
        }
    except FileNotFoundError:
        print(f"❌ ERROR: The domain at '{REPO_BASE_DIR}' could not be found.")
        return set()

def perform_archiving_ritual(repo_name):
    """Copies the README.md from a given repository to the README_HUB."""
    source_readme = REPO_BASE_DIR / repo_name / "README.md"

    if source_readme.is_file():
        target_dir = README_HUB_DIR / repo_name
        target_dir.mkdir(parents=True, exist_ok=True)
        renamed_readme = f"{repo_name}_README.md"
        target_path = target_dir / renamed_readme
        # Use copy2 to preserve metadata, including the original modification time.
        shutil.copy2(source_readme, target_path)
        print(f"🗂️  Archived README for '{repo_name}'")

if __name__ == "__main__":
    print("🗂️  Awakening the Archivist...")
    README_HUB_DIR.mkdir(exist_ok=True)

    discovered_repos = get_repo_dirs()

    if discovered_repos:
        print(f"🔎 Found {len(discovered_repos)} repositories to archive. Beginning the ritual...")
        for repo in sorted(list(discovered_repos)):
            perform_archiving_ritual(repo)
        print("\n✅ The Archivist's work is complete. The Memory Palace has been populated.")
    else:
        print("\n⚠️ No repositories found in the domain to archive.")
