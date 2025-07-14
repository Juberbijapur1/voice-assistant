#!/usr/bin/env python3
"""
Setup script for Voice Assistant
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def check_microphone():
    """Check if microphone is available"""
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Microphone detected and working!")
            return True
    except Exception as e:
        print(f"❌ Microphone error: {e}")
        print("💡 Make sure your microphone is connected and working")
        return False

if __name__ == "__main__":
    print("🚀 Setting up Voice Assistant...")
    
    if install_requirements():
        if check_microphone():
            print("\n🎉 Setup complete! You can now run: python voice_model.py")
        else:
            print("\n⚠️  Setup completed but microphone check failed.")
            print("   You may need to check your microphone settings.")
    else:
        print("\n❌ Setup failed. Please check the error messages above.") 