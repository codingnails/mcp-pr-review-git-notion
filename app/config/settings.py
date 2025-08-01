import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

    @classmethod
    def validate(cls):
        missing = [k for k, v in cls.__dict__.items()
                   if not k.startswith("__") and v is None]
        if missing:
            raise ValueError(f"Missing env vars: {', '.join(missing)}")

Settings.validate()
