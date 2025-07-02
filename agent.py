from livekit.agents import Agent, RunContext, function_tool
from livekit.agents import run_server
from tools import *

agent = Agent(
    voice_config={"language_code": "en-US"},
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
    ]
)

if __name__ == "__main__":
    run_server(agent)
