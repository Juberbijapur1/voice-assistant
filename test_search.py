#!/usr/bin/env python3
"""
Test script to demonstrate application search functionality
"""

import os
import winreg
from voice_assistant_enhanced import search_applications

def test_search():
    """Test the search functionality with common applications"""
    
    test_apps = [
        "chrome",
        "notepad", 
        "calculator",
        "word",
        "excel",
        "paint",
        "explorer",
        "cmd",
        "powershell",
        "code",  # VS Code
        "spotify",
        "discord",
        "steam"
    ]
    
    print("🔍 Testing Application Search Functionality")
    print("=" * 50)
    
    for app in test_apps:
        print(f"\n🔎 Searching for: {app}")
        found_apps = search_applications(app)
        
        if found_apps:
            print(f"✅ Found {len(found_apps)} application(s):")
            for i, app_path in enumerate(found_apps[:3], 1):  # Show first 3 results
                print(f"   {i}. {os.path.basename(app_path)}")
                print(f"      Path: {app_path}")
            if len(found_apps) > 3:
                print(f"   ... and {len(found_apps) - 3} more")
        else:
            print(f"❌ No applications found for '{app}'")
    
    print("\n" + "=" * 50)
    print("✅ Search test completed!")

if __name__ == "__main__":
    test_search() 