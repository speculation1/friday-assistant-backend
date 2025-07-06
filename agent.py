import asyncio
import os
import logging
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent
from tools import tools

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Verify required environment variables
required_env = [
    "LIVEKIT_URL", "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET",
    "GMAIL_USER", "GMAIL_APP_PASSWORD", "NEWS_API_KEY"
]

missing = [var for var in required_env if not os.getenv(var)]
if missing:
    raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")

async def main():
    # Create the agent
    agent = Agent(
        tools=tools,
        instructions="You are Friday, a helpful mobile assistant created by Austine."
    )

    # Configure worker options
    worker_options = agents.WorkerOptions(
        worker_type="agent",
        room_name="assistant-room",
        identity="friday-bot",
        connect_options=agents.ConnectOptions(
            url=os.getenv("LIVEKIT_URL"),
            api_key=os.getenv("LIVEKIT_API_KEY"),
            api_secret=os.getenv("LIVEKIT_API_SECRET"),
        )
    )

    # Create and run worker
    worker = agents.create_worker(agent, worker_options)
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())