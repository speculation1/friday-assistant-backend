import asyncio
from livekit.agents import Agent
from tools import tools  # Your defined function_tool list

async def main():
    agent = Agent(
        tools=tools  # ✅ ONLY 'tools' is accepted in v1.1.5
    )

    async with agent.run_in_background():
        print("🟢 Friday is running...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
