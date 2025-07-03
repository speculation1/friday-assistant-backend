from livekit.agents.server import run_server
from tools import tools

if __name__ == "__main__":
    run_server(
        tools=tools,
        instructions="You are Friday, a helpful and smart assistant.",
    )
