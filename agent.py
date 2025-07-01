from livekit.agents import function_tool, assistant, RunContext, Agent, VoiceConfig
from tools import *
import os

my_agent = Agent(
    name="Friday",
    voice_config=VoiceConfig.from_language_code("en-US"),
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

assistant.run_server(my_agent)
