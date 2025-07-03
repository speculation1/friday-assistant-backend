import asyncio
from livekit.agents import Agent
from livekit.agents.server import run_server  # ✅ Only works in v1.1.5
from tools import tools  # your list of @function_tool()

async def main():
    agent = Agent(
        instructions="You are Friday, a smart assistant built to help with everyday tasks.",
        tools=tools,
    )

    await run_server(agent)  # ✅ Correct for 1.1.5

if __name__ == "__main__":
    asyncio.run(main())
