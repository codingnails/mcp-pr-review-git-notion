from integrations.github_client import GitHubClient
from typing import Dict, Any
import sys
import traceback

async def fetch_pr(repo_owner: str, repo_name: str, pr_number: int) -> Dict[str, Any]:
            """Fetch changes from a GitHub pull request."""
            print(f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}", file=sys.stderr)
            try:
                pr_info = GitHubClient().fetch_pr_changes(repo_owner, repo_name, pr_number)
                if pr_info is None:
                    print("No changes returned from fetch_pr_changes", file=sys.stderr)
                    return {}
                print(f"Successfully fetched PR information", file=sys.stderr)
                return pr_info
            except Exception as e:
                print(f"Error fetching PR: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}