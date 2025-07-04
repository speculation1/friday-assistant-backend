import asyncio
import os
import logging
from dotenv import load_dotenv
from livekit.agents import Agent
from tools import tools

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Ensure required environment variables are present
required_env = [
    "GMAIL_USER", "GMAIL_APP_PASSWORD",
    "NEWS_API_KEY",
    "LIVEKIT_URL", "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET"
]

missing = [var for var in required_env if not os.getenv(var)]
if missing:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")

async def main():
    agent = Agent(
        tools=tools,
        instructions="You are Friday, a helpful mobile assistant created by Austine. Respond clearly and concisely.",
        url=os.getenv("LIVEKIT_URL"),
        api_key=os.getenv("LIVEKIT_API_KEY"),
        api_secret=os.getenv("LIVEKIT_API_SECRET"),
    )

    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
