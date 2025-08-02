import sys
import traceback
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP
from app.tools.github_tools import fetch_pr
from app.tools.notion_tools import create_notion_page
from app.integrations.github_client import GitHubClient
from app.integrations.notion_client import NotionClient

class PRAnalyzer:
    def __init__(self):
        
        # Initialize MCP Server
        self.mcp = FastMCP("github_pr_analysis")
        print("MCP Server initialized", file=sys.stderr)
        
        # Initialize Notion client
        self.notion_client = NotionClient()

        # Initialize GitHub client
        self.github_client = GitHubClient()
        
        # Register MCP tools
        self._register_tools()
    
    def _register_tools(self):
        """Register MCP tools for PR analysis."""
        self.mcp.tool()(fetch_pr)
        self.mcp.tool()(create_notion_page)
    
    def run(self):
        """Start the MCP server."""
        try:
            print("Running MCP Server for GitHub PR Analysis...", file=sys.stderr)
            self.mcp.run(transport="stdio")
        except Exception as e:
            print(f"Fatal Error in MCP Server: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    analyzer = PRAnalyzer()
    analyzer.run() 