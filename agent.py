import asyncio
from livekit.agents import Agent
from tools import tools  # This should point to your defined @function_tool functions

async def main():
    agent = Agent(
        name="Friday",       # Optional, defaults to "Agent"
        tools=tools,         # Your tools list from tools.py
        agent_id="friday",   # Optional: useful for logging or identifying the agent
    )

    async with agent.run_in_background():
        print("🟢 Friday is running...")
        await asyncio.Event().wait()  # Keeps the agent running indefinitely

if __name__ == "__main__":
    asyncio.run(main())
