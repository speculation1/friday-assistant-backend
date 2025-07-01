from livekit.agents import function_tool, RunContext, Agent
from tools import *
import os

# Check if the newer VoiceConfig import exists
try:
    from livekit.agents.config import VoiceConfig
except ImportError:
    VoiceConfig = None

# Set up the agent
my_agent = Agent(
    name="Friday",
    voice_config=VoiceConfig.from_language_code("en-US") if VoiceConfig else None,
    tools=[
        get_weather,
        search_web,
        make_call,
        notify_incoming_call,
        battery_status,
        play_music,
        take_photo,
        add_appointment,
        get_local_time,
        send_email,
        translate_text,
        get_news,
        get_traffic_details,
        analyze_appearance,
        request_app_lock
    ],
)

# Fallback to older server run
if hasattr(my_agent, "start_server"):
    my_agent.start_server()
else:
    import livekit.agents.assistant as assistant
    assistant.run_server(my_agent)
