from app.config.settings import Settings
from notion_client import Client
import sys
import traceback

class NotionClient:
    def __init__(self):
        """Initialize the Notion client with API key and page ID."""
        try:
            self.notion_api_key = Settings.NOTION_API_KEY
            self.notion_page_id = Settings.NOTION_PAGE_ID
            
            if not self.notion_api_key or not self.notion_page_id:
                raise ValueError("Missing Notion API key or page ID in environment variables")
            
            self.notion = Client(auth=self.notion_api_key)
            print(f"Notion client initialized successfully", file=sys.stderr)
            print(f"Using Notion page ID: {self.notion_page_id}", file=sys.stderr)
        except Exception as e:
            print(f"Error initializing Notion client: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)

    def create_page(self, title: str, content: str) -> str:
            """Create a Notion page with PR analysis."""
            print(f"Creating Notion page: {title}", file=sys.stderr)
            try:
                self.notion.pages.create(
                    parent={"type": "page_id", "page_id": self.notion_page_id},
                    properties={"title": {"title": [{"text": {"content": title}}]}},
                    children=[{
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{
                                "type": "text",
                                "text": {"content": content}
                            }]
                        }
                    }]
                )
                print(f"Notion page '{title}' created successfully!", file=sys.stderr)
                return f"Notion page '{title}' created successfully!"
            except Exception as e:
                error_msg = f"Error creating Notion page: {str(e)}"
                print(error_msg, file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return error_msg