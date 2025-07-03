import asyncio
from livekit.agents import Agent
from livekit.agents.server import run_server

from tools import tools

async def main():
    
    agent = Agent(
        instructions="You are Friday, a smart assistant built to help with everyday tasks.",
        tools=tools,
    )
    await run_server(agent)

if __name__ == "__main__":
    asyncio.run(main())
