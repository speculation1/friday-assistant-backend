import asyncio
from livekit.agents import Agent
from tools import tools  # This imports the list you just defined

async def main():
    agent = Agent(
        tools=tools,
        description="Your smart assistant Friday",
    )

    async with agent.run_in_background():
        print("🟢 Friday is running...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
