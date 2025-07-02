# Include the tool functions you provided earlier
import logging
from livekit.agents import function_tool, RunContext
import requests
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional
from duckduckgo_search import DDGS
from googletrans import Translator
import newsapi

from datetime import datetime
import pytz

# -----------------------
# WEATHER
# -----------------------
@function_tool()
async def get_weather(context: RunContext, city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}."


# -----------------------
# WEB SEARCH
# -----------------------
@function_tool()
async def search_web(context: RunContext, query: str, max_results: int = 5) -> str:
    """
    Perform a web search using DuckDuckGo and return the top results, including image search.
    """
    try:
        with DDGS() as ddgs:
            # Text search
            text_results = ddgs.text(query, max_results=max_results)
            output = "Web search results:\n"
            for r in text_results:
                title = r.get("title", "No title")
                link = r.get("href", "No link")
                snippet = r.get("body", "")
                output += f"\nTitle: {title}\nLink: {link}\nSnippet: {snippet}\n\n"

            # Image search
            image_results = ddgs.images(query, max_results=max_results)
            if image_results:
                output += "\nImage results:\n"
                for i in image_results:
                    title = i.get("title", "No title")
                    image_url = i.get("image", "No image URL")
                    output += f"Title: {title}\nImage URL: {image_url}\n\n"

            return output.strip()
    except Exception as e:
        return f"Search failed: {e}"


# -----------------------
# PHONE FUNCTIONS (Mocked)
# -----------------------
@function_tool()
async def make_call(context: RunContext, phone_number: str) -> str:
    """Place a call to the given phone number."""
    logging.info(f"Calling {phone_number}...")
    return f"Calling {phone_number} now."


@function_tool()
async def notify_incoming_call(context: RunContext, caller_id: str) -> str:
    """Notify of an incoming call."""
    return f"Incoming call from {caller_id}."


@function_tool()
async def battery_status(context: RunContext, level: int, is_charging: bool) -> str:
    """Notify battery level and charging status."""
    if is_charging and level == 100:
        return "Battery is fully charged."
    elif not is_charging and level <= 15:
        return "Battery is low. Please charge your device."
    return f"Battery level is {level}%. Charging: {'Yes' if is_charging else 'No'}."


@function_tool()
async def play_music(context: RunContext, song_name: str) -> str:
    """Play a song from the device."""
    return f"Playing {song_name}."


@function_tool()
async def take_photo(context: RunContext, camera: str = "rear") -> str:
    """Take a photo using the specified camera."""
    return f"Taking photo with the {camera} camera."


@function_tool()
async def add_appointment(context: RunContext, title: str, time: str) -> str:
    """Save an appointment."""
    return f"Appointment '{title}' saved for {time}."



@function_tool()
async def get_local_time(context: RunContext, country: str) -> str:
    """
    Get the current local time in the specified country.
    """
    try:
        # Convert country to timezone
        country = country.strip().lower()
        timezone_map = {
            "nigeria": "Africa/Lagos",
            "united states": "America/New_York",
            "uk": "Europe/London",
            "germany": "Europe/Berlin",
            "india": "Asia/Kolkata",
            "china": "Asia/Shanghai",
            "japan": "Asia/Tokyo",
            "australia": "Australia/Sydney"
            # Add more countries as needed
        }

        if country not in timezone_map:
            return f"Sorry, I don't have timezone information for {country}."

        timezone = pytz.timezone(timezone_map[country])
        local_time = datetime.now(timezone).strftime("%I:%M %p on %A, %B %d, %Y")
        return f"The current time in {country.title()} is {local_time}."
    
    except Exception as e:
        return f"An error occurred while getting time for {country}: {str(e)}"




@function_tool()    
async def send_email(
    context: RunContext,  # type: ignore
    to_email: str,
    subject: str,
    message: str,
    cc_email: Optional[str] = None
) -> str:
    """
    Send an email through Gmail.
    
    Args:
        to_email: Recipient email address
        subject: Email subject line
        message: Email body content
        cc_email: Optional CC email address
    """
    try:
        # Gmail SMTP configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # Get credentials from environment variables
        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")  # Use App Password, not regular password
        
        if not gmail_user or not gmail_password:
            logging.error("Gmail credentials not found in environment variables")
            return "Email sending failed: Gmail credentials not configured."
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add CC if provided
        recipients = [to_email]
        if cc_email:
            msg['Cc'] = cc_email
            recipients.append(cc_email)
        
        # Attach message body
        msg.attach(MIMEText(message, 'plain'))
        
        # Connect to Gmail SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(gmail_user, gmail_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(gmail_user, recipients, text)
        server.quit()
        
        logging.info(f"Email sent successfully to {to_email}")
        return f"Email sent successfully to {to_email}"
        
    except smtplib.SMTPAuthenticationError:
        logging.error("Gmail authentication failed")
        return "Email sending failed: Authentication error. Please check your Gmail credentials."
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
        return f"Email sending failed: SMTP error - {str(e)}"
    except Exception as e:
        logging.error(f"Error sending email: {e}")
        return f"An error occurred while sending email: {str(e)}"

# -----------------------
# NEW TOOLS
# -----------------------

@function_tool()
async def translate_text(context: RunContext, text: str, dest_language: str) -> str:
    """Translate text to a destination language."""
    try:
        translator = Translator()
        translated = translator.translate(text, dest=dest_language)
        return f"Translated text: {translated.text}"
    except Exception as e:
        return f"Translation failed: {e}"


@function_tool()
async def get_news(context: RunContext, query: str, max_results: int = 5) -> str:
    """Get the latest news headlines."""
    try:
        news_api_key = os.getenv("NEWS_API_KEY")
        if not news_api_key:
            return "News API key not configured."

        news_api = newsapi.NewsApiClient(api_key=news_api_key)
        top_headlines = news_api.get_top_headlines(q=query, language='en', page_size=max_results)

        output = ""
        for article in top_headlines['articles']:
            title = article.get('title', 'No title')
            url = article.get('url', 'No URL')
            output += f"\nTitle: {title}\nLink: {url}\n"
        return output.strip()
    except Exception as e:
        return f"Failed to get news: {e}"


@function_tool()
async def get_traffic_details(context: RunContext, location: str) -> str:
    """Get traffic details for a location (mocked)."""
    return f"Getting traffic details for {location}. Currently, traffic is moderate."


@function_tool()
async def analyze_appearance(context: RunContext, image_data: str) -> str:
    """
    Analyzes an image of a person's outfit and provides fashion advice.
    `image_data` should be a base64 string or URL.
    """
    # You may later decode base64 or fetch image from URL
    return "You look sharp! The colors complement each other well. Perhaps add a watch to complete the look."


@function_tool()
async def request_app_lock(context: RunContext, app_name: str) -> str:
    """
    Requests the client application to lock a specific app.
    """
    # This function sends a structured message to the client.
    # The client-side (Flutter app) will be responsible for interpreting this and locking the app.
    return f'{{"action": "lock_app", "target": "{app_name}"}}'


# -----------------------
# Example search usage
# -----------------------
if __name__ == "__main__":
    query = "How to start a building materials business in Nigeria"
    # This will now error because search_web is async
    # import asyncio
    # async def main():
    #     results = await search_web(None, query)
    #     print(results)
    # asyncio.run(main())
tools = [
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
    request_app_lock,
]

