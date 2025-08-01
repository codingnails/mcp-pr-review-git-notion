# GitHub PR Review MCP Server

A modular MCP (Model Context Protocol) server that integrates GitHub Pull Request data, analyzes code changes using Anthropic's Claude Desktop, and saves PR review summaries to Notion.

---

## Overview

This project demonstrates how to build an MCP server using Anthropic’s Model Context Protocol (MCP) to enable large language models (LLMs) like Claude to interact dynamically with external tools:

- Fetch pull request details and changed files from GitHub.
- Analyze PR code changes with Claude Desktop.
- Create structured PR review documentation in Notion.

---

## Features

- Standardized MCP server architecture with modular tools.
- GitHub integration for fetching PR metadata and diffs.
- Notion integration for saving PR analysis as pages.
- Uses Python, MCP, `requests`, `notion-client`, and `python-dotenv`.

---

## Data Flow

```

   +---------------------------+
   | 1. User Input in Claude   |
   |    Desktop (PR Link)      |
   +------------+--------------+
                |
                v
   +---------------------------+
   | 2. MCP Client sends       |
   |    request to MCP Server  |
   +------------+--------------+
                |
                v
   +---------------------------+
   | 3. MCP Server runs fetch_pr|
   |    tool → Calls GitHub API|
   +------------+--------------+
                |
                v
   +---------------------------+
   | 4. GitHub API returns PR  |
   |    metadata & file changes|
   +------------+--------------+
                |
                v
   +---------------------------+
   | 5. Claude Desktop analyzes|
   |    PR data & generates    |
   |    review summary         |
   +------------+--------------+
                |
                v
   +---------------------------+
   | 6. User requests to save  |
   |    review → MCP Server's  |
   |    create_notion_page tool|
   +------------+--------------+
                |
                v
   +---------------------------+
   | 7. MCP Server calls       |
   |    Notion API to create   |
   |    page with summary      |
   +------------+--------------+
                |
                v
   +---------------------------+
   | 8. Notion page created in |
   |    configured workspace   |
   +---------------------------+


```

---


## Setup & Usage

```

1. Clone the repository
2. Create a `.env` file with:
   GITHUB\_TOKEN=your\_github\_token
   NOTION\_API\_KEY=your\_notion\_api\_key
   NOTION\_PAGE\_ID=your\_notion\_page\_id
3. Install dependencies:
   pip install -r requirements.txt
4. Run the MCP server:
   python -m app.pr\_analyzer
5. Use Claude Desktop MCP plugin to connect and use tools

```

---

Let me know if you want me to tweak the formatting or add more details!
