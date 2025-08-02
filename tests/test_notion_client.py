from unittest.mock import patch, MagicMock
from app.integrations.notion_client import NotionClient


@patch("app.integrations.notion_client.Client")
def test_create_notion_page_success(mock_create):
    mock_client_instance = MagicMock()
    mock_create.return_value = mock_client_instance
    mock_client_instance.pages.create.return_value = {"id": "123"}
    result = NotionClient().create_page("Test Title", "Test Content")
    assert "created successfully" in result.lower()


@patch("app.integrations.notion_client.Client")
def test_create_notion_page_failure(mock_create):
    mock_client_instance = MagicMock()
    mock_create.return_value = mock_client_instance
    mock_client_instance.pages.create.side_effect = Exception("Notion API error")
    result = NotionClient().create_page("Test Title", "Test Content")
    assert "error" in result.lower()
