from pathlib import Path
from config import REPO_BASE_DIR, README_HUB_DIR

def survey_the_domain():
    """
    Scans the base directory for all project repositories.
    This is the essence of The Digital Surveyor.
    """
    print(f"🔭 Surveying the domain: {REPO_BASE_DIR}")
    try:
        # Discover all paths, filter for directories, and exclude the hub itself.
        all_dirs = {
            path.name for path in REPO_BASE_DIR.iterdir()
            if path.is_dir() and path.resolve() != README_HUB_DIR.resolve()
        }
        return all_dirs
    except FileNotFoundError:
        print(f"❌ ERROR: The domain at '{REPO_BASE_DIR}' could not be found.")
        return set()

if __name__ == "__main__":
    print("--- The Digital Surveyor ---")
    discovered_repos = survey_the_domain()

    if discovered_repos:
        print(f"\n✅ Survey complete. Found {len(discovered_repos)} repositories:")
        for repo in sorted(list(discovered_repos)):
            print(f"  - {repo}")
    else:
        print("\n⚠️ No repositories found in the domain.")
