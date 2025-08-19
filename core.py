import shutil
from config import REPO_BASE_DIR, README_HUB_DIR

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

def sync_repo_readme(repo_name):
    """
    Copies or updates the README.md for a single repository.
    Returns True if a file was copied/updated, False otherwise.
    """
    source_readme = REPO_BASE_DIR / repo_name / "README.md"
    if not source_readme.is_file():
        return False

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
        return True
    
    return False

def prune_deleted_repos(source_repos, hub_repos):
    """Removes directories from the hub that are no longer in the source."""
    deleted_repos = hub_repos - source_repos
    if deleted_repos:
        print(f"🧹 Found {len(deleted_repos)} deleted repositories. Pruning from Hub...")
        for repo_name in deleted_repos:
            shutil.rmtree(README_HUB_DIR / repo_name)
            print(f"🗑️ Removed '{repo_name}' from Hub.")