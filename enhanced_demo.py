#!/usr/bin/env python3
"""
Enhanced Voice Assistant Demo
============================

This demo showcases the advanced features of the voice assistant:

1. Opening Code Editors:
   - "open vs code" - Opens Visual Studio Code
   - "open cursor" - Opens Cursor editor
   - "open notepad" - Opens Notepad

2. HTML Code Generation:
   - "create html personal portfolio" - Creates HTML file
   - "make html business website" - Generates HTML code
   - "generate html blog page" - Creates HTML template

3. Math Problem Solving:
   - "solve math 5 plus 3" - Calculates 5 + 3
   - "calculate 10 times 5" - Calculates 10 * 5
   - "solve math 100 divided by 4" - Calculates 100 / 4

4. Interactive Features:
   - "hey partner" - Gets assistant's attention anytime
   - "time" - Tells current time
   - "date" - Tells current date
   - "stop" - Stops the assistant

5. Background Listening:
   - Assistant listens for "hey partner" even during task execution
   - Can interrupt ongoing tasks to respond to user

Usage:
    python enhanced_demo.py
"""

from enhanced_voice_assistant import EnhancedVoiceAssistant

def main():
    print("🚀 Enhanced Voice Assistant Demo")
    print("=" * 50)
    print()
    print("🎯 Features Available:")
    print("• Open code editors (VS Code, Cursor, Notepad)")
    print("• Create HTML files from voice descriptions")
    print("• Solve mathematical expressions")
    print("• Get time and date information")
    print("• Say 'hey partner' anytime for attention")
    print("• Background listening during tasks")
    print()
    print("💡 Example Commands:")
    print("• 'open vs code'")
    print("• 'create html personal portfolio'")
    print("• 'solve math 15 plus 25'")
    print("• 'time'")
    print("• 'hey partner'")
    print("• 'stop'")
    print()
    
    input("Press Enter to start the Enhanced Voice Assistant...")
    
    # Create and run the assistant
    assistant = EnhancedVoiceAssistant()
    
    try:
        assistant.run()
    except KeyboardInterrupt:
        print("\n👋 Demo stopped by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main() 