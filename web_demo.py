#!/usr/bin/env python3
"""
Demo script to showcase web-enabled voice assistant capabilities
"""

import webbrowser
import urllib.parse
import requests
from bs4 import BeautifulSoup
import datetime

def demo_web_search():
    """Demo web search functionality"""
    print("🔍 Web Search Demo:")
    print("=" * 40)
    
    # Example searches
    searches = [
        "Python programming tutorial",
        "latest technology news",
        "weather in London",
        "best restaurants near me"
    ]
    
    for search in searches:
        print(f"Searching for: {search}")
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(search)}"
        print(f"URL: {search_url}")
        print("-" * 40)

def demo_website_opening():
    """Demo website opening functionality"""
    print("\n🌐 Website Opening Demo:")
    print("=" * 40)
    
    # Popular websites
    websites = [
        "youtube.com",
        "facebook.com", 
        "twitter.com",
        "instagram.com",
        "gmail.com",
        "maps.google.com",
        "github.com",
        "stackoverflow.com"
    ]
    
    for site in websites:
        print(f"Opening: {site}")
        print(f"URL: https://{site}")
        print("-" * 40)

def demo_weather_api():
    """Demo weather API functionality"""
    print("\n🌤️ Weather API Demo:")
    print("=" * 40)
    
    # Note: This requires an API key from OpenWeatherMap
    print("To get weather data, you need to:")
    print("1. Sign up at https://openweathermap.org/api")
    print("2. Get a free API key")
    print("3. Replace 'YOUR_API_KEY' in web_voice_assistant.py")
    print("4. Then you can say: 'weather in London'")
    print("-" * 40)

def demo_time_date():
    """Demo time and date functionality"""
    print("\n🕐 Time & Date Demo:")
    print("=" * 40)
    
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    
    print(f"Current Time: {current_time}")
    print(f"Current Date: {current_date}")
    print("-" * 40)

def demo_voice_commands():
    """Demo available voice commands"""
    print("\n🎤 Voice Commands Demo:")
    print("=" * 40)
    
    commands = {
        "Web Search": [
            "search Python tutorial",
            "google latest news",
            "find weather in Mumbai"
        ],
        "Website Opening": [
            "open youtube",
            "go to facebook",
            "visit gmail",
            "open maps"
        ],
        "Social Media": [
            "open twitter",
            "go to instagram",
            "open facebook"
        ],
        "Information": [
            "what time is it",
            "what's the date today",
            "get news",
            "weather in Delhi"
        ],
        "Applications": [
            "open chrome",
            "open notepad",
            "open calculator",
            "open word"
        ]
    }
    
    for category, cmd_list in commands.items():
        print(f"\n{category}:")
        for cmd in cmd_list:
            print(f"  • Say: '{cmd}'")
    
    print("-" * 40)

def main():
    """Run all demos"""
    print("🚀 Web-Enabled Voice Assistant Demo")
    print("=" * 50)
    
    demo_web_search()
    demo_website_opening()
    demo_weather_api()
    demo_time_date()
    demo_voice_commands()
    
    print("\n🎯 To use the voice assistant:")
    print("1. Run: python web_voice_assistant.py")
    print("2. Say: 'help' for all commands")
    print("3. Try: 'search Python tutorial'")
    print("4. Try: 'open youtube'")
    print("5. Try: 'what time is it'")
    print("\n✨ Enjoy your web-enabled voice assistant!")

if __name__ == "__main__":
    main() 