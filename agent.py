from livekit.agents import Agent, RunContext
from tools import tools  # your list of tools
import asyncio

async def main():
    agent = Agent(
        tools=tools,
        description="Your smart assistant",
    )

    async with agent.run_in_background():
        print("Agent is running...")
        await asyncio.Event().wait()  # Keeps the agent alive

if __name__ == "__main__":
    asyncio.run(main())
