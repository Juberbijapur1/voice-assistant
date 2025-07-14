#!/usr/bin/env python3
"""
Demo script to showcase advanced voice assistant capabilities
"""

import webbrowser
import urllib.parse
import psutil
import datetime

def demo_close_functionality():
    """Demo app closing functionality"""
    print("❌ App Closing Demo:")
    print("=" * 40)
    
    # Show running processes
    print("Currently running processes:")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in ['chrome.exe', 'notepad.exe', 'calc.exe', 'mspaint.exe']:
                print(f"  • {proc.info['name']} (PID: {proc.info['pid']})")
        except:
            continue
    
    print("\nVoice commands to close apps:")
    close_commands = [
        "close chrome",
        "close notepad", 
        "close calculator",
        "close paint",
        "close youtube",
        "close facebook",
        "close gmail",
        "close [any app name]"
    ]
    
    for cmd in close_commands:
        print(f"  • Say: '{cmd}'")
    
    print("-" * 40)

def demo_enhanced_search():
    """Demo enhanced search functionality"""
    print("\n🔍 Enhanced Search Demo:")
    print("=" * 40)
    
    search_types = {
        "Video Search": [
            "search video Python tutorial",
            "search video cooking recipes",
            "find video music videos",
            "youtube search funny cats"
        ],
        "Image Search": [
            "search image sunset",
            "find image cute puppies",
            "search image beautiful landscapes"
        ],
        "News Search": [
            "search news technology",
            "find news sports",
            "search news weather"
        ],
        "Shopping Search": [
            "search shopping laptops",
            "find product smartphones",
            "search shopping headphones"
        ],
        "General Search": [
            "search Python programming",
            "google latest news",
            "find weather in Mumbai"
        ]
    }
    
    for category, searches in search_types.items():
        print(f"\n{category}:")
        for search in searches:
            print(f"  • Say: '{search}'")
    
    print("-" * 40)

def demo_website_commands():
    """Demo website opening and closing"""
    print("\n🌐 Website Commands Demo:")
    print("=" * 40)
    
    websites = {
        "Open Websites": [
            "open youtube",
            "go to facebook",
            "visit gmail",
            "open maps",
            "open twitter",
            "open instagram"
        ],
        "Close Websites": [
            "close youtube",
            "close facebook", 
            "close gmail",
            "close twitter",
            "close instagram"
        ]
    }
    
    for category, commands in websites.items():
        print(f"\n{category}:")
        for cmd in commands:
            print(f"  • Say: '{cmd}'")
    
    print("-" * 40)

def demo_app_commands():
    """Demo application commands"""
    print("\n💻 Application Commands Demo:")
    print("=" * 40)
    
    apps = {
        "Open Apps": [
            "open chrome",
            "open notepad",
            "open calculator",
            "open word",
            "open excel",
            "open paint",
            "open explorer"
        ],
        "Close Apps": [
            "close chrome",
            "close notepad",
            "close calculator",
            "close word",
            "close excel",
            "close paint"
        ]
    }
    
    for category, commands in apps.items():
        print(f"\n{category}:")
        for cmd in commands:
            print(f"  • Say: '{cmd}'")
    
    print("-" * 40)

def demo_information_commands():
    """Demo information commands"""
    print("\n📰 Information Commands Demo:")
    print("=" * 40)
    
    info_commands = [
        "what time is it",
        "what's the date today",
        "get news",
        "weather in London",
        "weather in Mumbai",
        "weather in New York"
    ]
    
    for cmd in info_commands:
        print(f"  • Say: '{cmd}'")
    
    print("-" * 40)

def demo_search_urls():
    """Show example search URLs"""
    print("\n🔗 Example Search URLs:")
    print("=" * 40)
    
    searches = [
        ("Video Search", "Python tutorial", "https://www.youtube.com/results?search_query=Python%20tutorial"),
        ("Image Search", "sunset", "https://www.google.com/search?q=sunset&tbm=isch"),
        ("News Search", "technology", "https://news.google.com/search?q=technology"),
        ("Shopping Search", "laptops", "https://www.google.com/search?q=laptops&tbm=shop"),
        ("General Search", "Python programming", "https://www.google.com/search?q=Python%20programming")
    ]
    
    for search_type, query, url in searches:
        print(f"\n{search_type}:")
        print(f"  Query: '{query}'")
        print(f"  URL: {url}")
    
    print("-" * 40)

def main():
    """Run all demos"""
    print("🚀 Advanced Voice Assistant Demo")
    print("=" * 50)
    
    demo_close_functionality()
    demo_enhanced_search()
    demo_website_commands()
    demo_app_commands()
    demo_information_commands()
    demo_search_urls()
    
    print("\n🎯 To use the advanced voice assistant:")
    print("1. Run: python advanced_voice_assistant.py")
    print("2. Say: 'help' for all commands")
    print("3. Try: 'search video Python tutorial'")
    print("4. Try: 'close chrome'")
    print("5. Try: 'open youtube'")
    print("6. Try: 'what time is it'")
    print("\n✨ Enjoy your advanced voice assistant!")

if __name__ == "__main__":
    main() 