import requests
import traceback
from config.settings import Settings


class GitHubClient:

    def __init__(self):
        self.token = Settings.GITHUB_TOKEN
        self.headers = {'Authorization': f'token {self.token}'}


    def fetch_pr_changes(self, repo_owner: str, repo_name: str, pr_number: int) -> list:
        """Fetch changes from a GitHub pull request.
        
        Args:
            repo_owner: The owner of the GitHub repository
            repo_name: The name of the GitHub repository
            pr_number: The number of the pull request to analyze
            
        Returns:
            A list of file changes with detailed information about each change
        """
        print(f" Fetching PR changes for {repo_owner}/{repo_name}#{pr_number}")
        
        # Fetch PR details
        pr_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
        files_url = f"{pr_url}/files"
        
        try:
            # Get PR metadata
            pr_response = requests.get(pr_url, headers=self.headers)
            pr_response.raise_for_status()
            pr_data = pr_response.json()
            
            # Get file changes
            files_response = requests.get(files_url, headers=self.headers)
            files_response.raise_for_status()
            files_data = files_response.json()
            
            # Add PR metadata
            pr_info = {
                'title': pr_data['title'],
                'description': pr_data['body'],
                'author': pr_data['user']['login'],
                'created_at': pr_data['created_at'],
                'updated_at': pr_data['updated_at'],
                'state': pr_data['state'],
                'total_changes': len(files_data),
                'changes': [{
                    'filename': file['filename'],
                    'status': file['status'],  # added, modified, removed
                    'additions': file['additions'],
                    'deletions': file['deletions'],
                    'changes': file['changes'],
                    'patch': file.get('patch', ''),  # The actual diff
                    'raw_url': file.get('raw_url', ''),
                    'contents_url': file.get('contents_url', '')
                }
                for file in files_data]
            }
            
            print(f"Successfully fetched {len(files_data)} files data")
            return pr_info
            
        except Exception as e:
            print(f"Error fetching PR changes: {str(e)}")
            traceback.print_exc()
            return None
