import asyncio
from livekit.agents import Agent, RunContext
from tools import tools  # This should be a list of @function_tool-decorated functions

async def main():
    agent = Agent(
        instructions="You are Friday, a smart voice assistant that helps with phone tasks and general inquiries.",
        tools=tools,
    )

    async with agent.run_in_background():
        print("🟢 Friday is running...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
