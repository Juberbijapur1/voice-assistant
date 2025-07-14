#!/usr/bin/env python3
"""
Demo script to showcase media voice assistant capabilities
"""

import webbrowser
import urllib.parse

def demo_play_commands():
    """Demo play functionality"""
    print("🎵 Play Commands Demo:")
    print("=" * 40)
    
    play_examples = {
        "Music Platforms": [
            "play hamari kahani on youtube",
            "play shape of you on spotify",
            "play despacito on apple music",
            "play bohemian rhapsody on amazon music",
            "play hotel california on deezer",
            "play stairway to heaven on soundcloud"
        ],
        "Video Platforms": [
            "play avengers on netflix",
            "play game of thrones on prime",
            "play frozen on disney",
            "play friends on hulu",
            "play breaking bad on netflix"
        ],
        "Alternative Formats": [
            "play music on spotify",
            "play bollywood songs on youtube",
            "play latest movies on netflix",
            "play comedy shows on prime"
        ]
    }
    
    for category, examples in play_examples.items():
        print(f"\n{category}:")
        for example in examples:
            print(f"  • Say: '{example}'")
    
    print("-" * 40)

def demo_platform_urls():
    """Show example platform URLs"""
    print("\n🔗 Platform URLs Demo:")
    print("=" * 40)
    
    platforms = {
        "YouTube": {
            "example": "hamari kahani",
            "url": "https://www.youtube.com/results?search_query=hamari%20kahani"
        },
        "Spotify": {
            "example": "shape of you",
            "url": "https://open.spotify.com/search/shape%20of%20you"
        },
        "Netflix": {
            "example": "avengers",
            "url": "https://www.netflix.com/search?q=avengers"
        },
        "Apple Music": {
            "example": "despacito",
            "url": "https://music.apple.com/search?term=despacito"
        },
        "Amazon Prime": {
            "example": "game of thrones",
            "url": "https://www.amazon.com/s?k=game%20of%20thrones&i=instant-video"
        },
        "Disney+": {
            "example": "frozen",
            "url": "https://www.disneyplus.com/search?q=frozen"
        }
    }
    
    for platform, info in platforms.items():
        print(f"\n{platform}:")
        print(f"  Example: 'play {info['example']} on {platform.lower()}'")
        print(f"  URL: {info['url']}")
    
    print("-" * 40)

def demo_voice_patterns():
    """Demo different voice command patterns"""
    print("\n🎤 Voice Command Patterns:")
    print("=" * 40)
    
    patterns = [
        "play [content] on [platform]",
        "play [song name] on [music platform]",
        "play [movie/show] on [video platform]",
        "play [artist] on [platform]",
        "play [genre] on [platform]"
    ]
    
    print("Supported Patterns:")
    for pattern in patterns:
        print(f"  • {pattern}")
    
    print("\nExamples:")
    examples = [
        "play hamari kahani on youtube",
        "play shape of you on spotify", 
        "play avengers on netflix",
        "play arijit singh on spotify",
        "play bollywood on youtube"
    ]
    
    for example in examples:
        print(f"  • '{example}'")
    
    print("-" * 40)

def demo_supported_platforms():
    """Show supported platforms"""
    print("\n🌐 Supported Platforms:")
    print("=" * 40)
    
    platforms = {
        "Music": [
            "YouTube",
            "Spotify", 
            "Apple Music",
            "Amazon Music",
            "Deezer",
            "SoundCloud"
        ],
        "Video": [
            "Netflix",
            "Amazon Prime",
            "Disney+",
            "Hulu"
        ],
        "General": [
            "Any website with search functionality"
        ]
    }
    
    for category, platform_list in platforms.items():
        print(f"\n{category}:")
        for platform in platform_list:
            print(f"  • {platform}")
    
    print("-" * 40)

def demo_usage_scenarios():
    """Demo real-world usage scenarios"""
    print("\n🎯 Usage Scenarios:")
    print("=" * 40)
    
    scenarios = [
        {
            "scenario": "Want to listen to a specific song",
            "command": "play hamari kahani on youtube",
            "action": "Opens YouTube and searches for 'hamari kahani'"
        },
        {
            "scenario": "Want to watch a movie",
            "command": "play avengers on netflix", 
            "action": "Opens Netflix and searches for 'avengers'"
        },
        {
            "scenario": "Want to listen to music on Spotify",
            "command": "play shape of you on spotify",
            "action": "Opens Spotify and searches for 'shape of you'"
        },
        {
            "scenario": "Want to watch a TV show",
            "command": "play friends on hulu",
            "action": "Opens Hulu and searches for 'friends'"
        },
        {
            "scenario": "Want to listen to an artist",
            "command": "play arijit singh on spotify",
            "action": "Opens Spotify and searches for 'arijit singh'"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. {scenario['scenario']}")
        print(f"   Command: '{scenario['command']}'")
        print(f"   Action: {scenario['action']}")
    
    print("-" * 40)

def main():
    """Run all demos"""
    print("🚀 Media Voice Assistant Demo")
    print("=" * 50)
    
    demo_play_commands()
    demo_platform_urls()
    demo_voice_patterns()
    demo_supported_platforms()
    demo_usage_scenarios()
    
    print("\n🎯 To use the media voice assistant:")
    print("1. Run: python media_voice_assistant.py")
    print("2. Say: 'help' for all commands")
    print("3. Try: 'play hamari kahani on youtube'")
    print("4. Try: 'play shape of you on spotify'")
    print("5. Try: 'play avengers on netflix'")
    print("6. Try: 'play arijit singh on spotify'")
    print("\n✨ Enjoy your media voice assistant!")

if __name__ == "__main__":
    main() 