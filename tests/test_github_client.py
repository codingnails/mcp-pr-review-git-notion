
import pytest
from unittest.mock import patch
from app.integrations.github_client import GitHubClient


@patch("app.integrations.github_client.requests.get")
def test_fetch_pr_changes_success(mock_get):
    # Mock PR metadata (first call)
    mock_get.return_value.json.side_effect = [
        {
            "title": "Test PR",
            "body": "PR description",
            "user": {"login": "testuser"},
            "created_at": "2025-08-01T00:00:00Z",
            "updated_at": "2025-08-01T00:00:00Z",
            "state": "open",
        },
        [
            {
                "filename": "file.py",
                "status": "modified",
                "additions": 5,
                "deletions": 2,
                "changes": 7,
            }
        ],
    ]
    mock_get.return_value.raise_for_status = lambda: None

    result = GitHubClient().fetch_pr_changes("owner", "repo", 1)
    assert result["title"] == "Test PR"
    assert result["total_changes"] == 1


@patch("app.integrations.github_client.requests.get")
def test_fetch_pr_changes_failure(mock_get):
    # Simulate API failure
    mock_get.side_effect = Exception("GitHub API failure")

    result = GitHubClient().fetch_pr_changes("owner", "repo", 1)
    assert result is None
