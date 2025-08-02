from app.integrations.notion_client import NotionClient
import sys
import traceback

async def create_notion_page(title: str, content: str) -> str:
            """Create a Notion page with PR analysis."""
            print(f"Creating Notion page: {title}", file=sys.stderr)
            try:
                NotionClient().create_page(title, content)
                print(f"Notion page '{title}' created successfully!", file=sys.stderr)
                return f"Notion page '{title}' created successfully!"
            except Exception as e:
                error_msg = f"Error creating Notion page: {str(e)}"
                print(error_msg, file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return error_msg    