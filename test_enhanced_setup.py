#!/usr/bin/env python3
"""
Test Enhanced Voice Assistant Setup
==================================

This script tests if all required dependencies are installed correctly.
"""

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import speech_recognition as sr
        print("✅ SpeechRecognition imported successfully")
    except ImportError as e:
        print(f"❌ SpeechRecognition import failed: {e}")
        return False
    
    try:
        import pyttsx3
        print("✅ pyttsx3 imported successfully")
    except ImportError as e:
        print(f"❌ pyttsx3 import failed: {e}")
        return False
    
    try:
        import subprocess
        import platform
        import os
        import winreg
        import re
        import math
        import threading
        import time
        from pathlib import Path
        from datetime import datetime
        print("✅ Standard library modules imported successfully")
    except ImportError as e:
        print(f"❌ Standard library import failed: {e}")
        return False
    
    return True

def test_microphone():
    """Test if microphone is accessible"""
    print("\n🎤 Testing microphone access...")
    
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        
        # Test microphone access
        with sr.Microphone() as source:
            print("✅ Microphone access successful")
            return True
    except Exception as e:
        print(f"❌ Microphone access failed: {e}")
        return False

def test_text_to_speech():
    """Test text-to-speech functionality"""
    print("\n🔊 Testing text-to-speech...")
    
    try:
        import pyttsx3
        engine = pyttsx3.init()
        
        # Test basic TTS
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.5)
        
        print("✅ Text-to-speech initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Text-to-speech initialization failed: {e}")
        return False

def main():
    print("🚀 Enhanced Voice Assistant Setup Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import test failed. Please install missing dependencies:")
        print("pip install -r requirements_enhanced.txt")
        return
    
    # Test microphone
    if not test_microphone():
        print("\n❌ Microphone test failed. Please check your microphone setup.")
        return
    
    # Test text-to-speech
    if not test_text_to_speech():
        print("\n❌ Text-to-speech test failed. Please check your audio setup.")
        return
    
    print("\n🎉 All tests passed! Your enhanced voice assistant is ready to use.")
    print("\n💡 To start the assistant, run:")
    print("python enhanced_demo.py")

if __name__ == "__main__":
    main() 