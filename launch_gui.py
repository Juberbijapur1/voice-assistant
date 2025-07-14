#!/usr/bin/env python3
"""
GUI Voice Assistant Launcher
============================

This script launches the GUI version of the enhanced voice assistant.
It includes error handling and setup verification.
"""

import sys
import tkinter as tk
from tkinter import messagebox

def check_dependencies():
    """Check if required dependencies are installed"""
    missing_deps = []
    
    try:
        import speech_recognition as sr
    except ImportError:
        missing_deps.append("SpeechRecognition")
    
    try:
        import pyttsx3
    except ImportError:
        missing_deps.append("pyttsx3")
    
    try:
        import tkinter
    except ImportError:
        missing_deps.append("tkinter")
    
    return missing_deps

def show_error_dialog(title, message):
    """Show error dialog"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror(title, message)
    root.destroy()

def show_info_dialog(title, message):
    """Show info dialog"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo(title, message)
    root.destroy()

def main():
    print("🚀 Launching Enhanced Voice Assistant GUI...")
    print("=" * 50)
    
    # Check dependencies
    missing_deps = check_dependencies()
    if missing_deps:
        error_msg = f"Missing dependencies: {', '.join(missing_deps)}\n\n"
        error_msg += "Please install them using:\n"
        error_msg += "pip install -r requirements_enhanced.txt"
        show_error_dialog("Missing Dependencies", error_msg)
        print(f"❌ Missing dependencies: {missing_deps}")
        return
    
    print("✅ All dependencies found")
    
    # Try to import the GUI
    try:
        from voice_assistant_gui import VoiceAssistantGUI
        print("✅ GUI module imported successfully")
    except ImportError as e:
        error_msg = f"Could not import GUI module: {e}\n\n"
        error_msg += "Make sure voice_assistant_gui.py is in the same directory."
        show_error_dialog("Import Error", error_msg)
        print(f"❌ Import error: {e}")
        return
    
    # Test microphone access
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("✅ Microphone access verified")
    except Exception as e:
        error_msg = f"Microphone access failed: {e}\n\n"
        error_msg += "Please check your microphone setup and permissions."
        show_error_dialog("Microphone Error", error_msg)
        print(f"❌ Microphone error: {e}")
        return
    
    # Test text-to-speech
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.5)
        print("✅ Text-to-speech initialized")
    except Exception as e:
        error_msg = f"Text-to-speech initialization failed: {e}\n\n"
        error_msg += "Please check your audio setup."
        show_error_dialog("Audio Error", error_msg)
        print(f"❌ Audio error: {e}")
        return
    
    print("🎉 All systems ready!")
    print("\n💡 GUI Features:")
    print("• Start/Stop voice listening with buttons")
    print("• Quick action buttons for common tasks")
    print("• Real-time activity log")
    print("• Voice command help")
    print("• Visual status indicators")
    
    # Launch GUI
    try:
        root = tk.Tk()
        app = VoiceAssistantGUI(root)
        
        # Handle window close
        def on_closing():
            if app.is_listening:
                app.stop_listening()
            root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        print("\n🖥️ GUI launched successfully!")
        print("💡 Tips:")
        print("• Click 'Start Listening' to begin voice recognition")
        print("• Use quick action buttons for instant tasks")
        print("• Say 'hey partner' anytime to get attention")
        print("• Check the activity log for detailed feedback")
        
        root.mainloop()
        
    except Exception as e:
        error_msg = f"Failed to launch GUI: {e}\n\n"
        error_msg += "Please check if tkinter is properly installed."
        show_error_dialog("Launch Error", error_msg)
        print(f"❌ Launch error: {e}")

if __name__ == "__main__":
    main() 