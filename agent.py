from livekit.agents import function_tool, RunContext, Agent
from livekit.agents.runtime import run_server
from tools import *

agent = Agent(
    voice="en-US",
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

run_server(agent)
