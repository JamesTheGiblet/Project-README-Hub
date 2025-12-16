import argparse
import time
from config import README_HUB_DIR, SCAN_INTERVAL
import core

def run_survey():
    """Performs the Digital Surveyor's duty: scan and list."""
    print("--- 🔭 The Digital Surveyor ---")
    discovered_repos = core.get_source_repo_dirs()
    if discovered_repos:
        print(f"\n✅ Survey complete. Found {len(discovered_repos)} repositories:")
        for repo in sorted(list(discovered_repos)):
            print(f"  - {repo}")
    else:
        print("\n⚠️ No repositories found in the domain.")

def run_archive():
    """Performs the Archivist's duty: a one-time sync of all READMEs."""
    print("--- 🗂️ The Archivist ---")
    discovered_repos = core.get_source_repo_dirs()
    if discovered_repos:
        print(f"🔎 Found {len(discovered_repos)} repositories to archive. Beginning the ritual...")
        update_count = 0
        for repo in sorted(list(discovered_repos)):
            if core.sync_repo_readme(repo):
                update_count += 1
        print(f"\n✅ The Archivist's work is complete. {update_count} READMEs archived/updated.")
    else:
        print("\n⚠️ No repositories found in the domain to archive.")

def run_watch():
    """Performs the Custodian's duty: continuous, full synchronization."""
    print("--- 🧹 The Custodian's Watch ---")
    print("Continuously monitoring for new, updated, and deleted repositories...")
    print("Press Ctrl+C to stop.")
    while True:
        try:
            print(f"\n--- Beginning sync cycle... (Next cycle in {SCAN_INTERVAL}s) ---")
            source_repos = core.get_source_repo_dirs()
            hub_repos = core.get_hub_repo_dirs()

            print(f"🔎 Checking {len(source_repos)} source repositories for updates...")
            for repo in source_repos:
                core.sync_repo_readme(repo)

            core.prune_deleted_repos(source_repos, hub_repos)

            print("✅ Sync cycle complete.")
            time.sleep(SCAN_INTERVAL)
        except KeyboardInterrupt:
            print("\n🛑 The Custodian's watch has ended. Goodbye!")
            break

def main():
    parser = argparse.ArgumentParser(description="The README Hub: A Memory Palace for Code.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Available rituals')

    subparsers.add_parser('survey', help="🔭 Survey the domain and list all found repositories.").set_defaults(func=run_survey)
    subparsers.add_parser('archive', help="🗂️  Perform a one-time archive of all READMEs.").set_defaults(func=run_archive)
    subparsers.add_parser('watch', help="🧹 Begin the continuous watch to keep the Hub synchronized.").set_defaults(func=run_watch)

    args = parser.parse_args()
    
    README_HUB_DIR.mkdir(exist_ok=True)
    
    args.func()

if __name__ == "__main__":
    main()