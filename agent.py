import asyncio
from livekit.agents import Agent
from tools import tools  # Import your list of tool functions

async def main():
    agent = Agent(
        name="Friday",
        instructions="You are Friday, a smart assistant that helps the user with real-time voice tasks.",
        tools=tools,
    )

    async with agent.run_in_background():
        print("🟢 Friday is running...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
