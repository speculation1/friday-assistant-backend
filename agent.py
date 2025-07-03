import asyncio
from livekit.agents import Agent
from tools import tools  # This should be your list of @function_tool() functions

async def main():
    agent = Agent(
        instructions="You are Friday, a smart assistant built to help with everyday tasks.",
        tools=tools
    )

    async with agent.run_in_background():
        print("🟢 Friday is running...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
