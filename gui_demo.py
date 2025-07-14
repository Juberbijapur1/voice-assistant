#!/usr/bin/env python3
"""
GUI Voice Assistant Demo
=======================

This demo showcases the GUI version of the enhanced voice assistant.

Features:
• Visual interface with buttons and controls
• Real-time activity log
• Quick action buttons for common tasks
• Start/Stop voice listening controls
• Voice command help display
• Status indicators

Usage:
    python gui_demo.py
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def show_gui_info():
    """Show information about the GUI features"""
    info_text = """
🎤 Enhanced Voice Assistant GUI
===============================

🖥️ GUI Features:
• Start/Stop Listening: Control voice recognition with buttons
• Quick Actions: Instant buttons for common tasks
• Activity Log: Real-time display of all actions and responses
• Status Display: Visual indicators of current state
• Voice Commands Help: Built-in command reference

🎯 Quick Action Buttons:
• 💻 Open VS Code - Launches Visual Studio Code
• 📝 Open Notepad - Opens Notepad editor
• 🌐 Create HTML - Generates sample HTML file
• 🧮 Solve Math - Calculates 5 + 3
• ⏰ Get Time - Shows current time

🎤 Voice Commands:
• "open vs code" - Opens Visual Studio Code
• "create html personal portfolio" - Creates HTML file
• "solve math 15 plus 25" - Calculates math problems
• "hey partner" - Gets assistant's attention anytime
• "time" - Tells current time
• "stop" - Stops the assistant

💡 Tips:
• Click 'Start Listening' to begin voice recognition
• Use quick action buttons for instant tasks
• Check the activity log for detailed feedback
• Say 'hey partner' anytime to get attention
• The GUI runs in the background while listening
    """
    
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("GUI Voice Assistant Demo", info_text)
    root.destroy()

def check_gui_file():
    """Check if GUI file exists"""
    if not os.path.exists("voice_assistant_gui.py"):
        print("❌ voice_assistant_gui.py not found!")
        print("Please make sure the GUI file is in the current directory.")
        return False
    return True

def launch_gui():
    """Launch the GUI voice assistant"""
    try:
        subprocess.run([sys.executable, "launch_gui.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch GUI: {e}")
    except FileNotFoundError:
        print("❌ launch_gui.py not found!")
        print("Please make sure all files are in the current directory.")

def main():
    print("🚀 GUI Voice Assistant Demo")
    print("=" * 50)
    print()
    
    # Check if GUI file exists
    if not check_gui_file():
        return
    
    print("✅ GUI files found")
    print()
    
    # Show GUI information
    show_gui_info()
    
    print("💡 GUI Features Available:")
    print("• Visual interface with buttons and controls")
    print("• Real-time activity log")
    print("• Quick action buttons for common tasks")
    print("• Start/Stop voice listening controls")
    print("• Voice command help display")
    print("• Status indicators")
    print()
    
    # Ask user if they want to launch GUI
    try:
        response = input("🎯 Would you like to launch the GUI now? (y/n): ").lower().strip()
        if response in ['y', 'yes', '']:
            print("\n🚀 Launching GUI Voice Assistant...")
            launch_gui()
        else:
            print("\n💡 To launch the GUI later, run:")
            print("python launch_gui.py")
            print("or")
            print("python voice_assistant_gui.py")
    except KeyboardInterrupt:
        print("\n👋 Demo cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main() 