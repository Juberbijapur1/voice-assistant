import speech_recognition as sr
import subprocess
import platform
import os
import winreg
import glob
from pathlib import Path
import time
import pyttsx3
import threading

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speech_engine = pyttsx3.init()
        self.setup_speech_engine()
        
    def setup_speech_engine(self):
        """Configure the text-to-speech engine"""
        try:
            # Get available voices
            voices = self.speech_engine.getProperty('voices')
            
            # Try to set a female voice if available
            for voice in voices:
                if "female" in voice.name.lower() or "zira" in voice.name.lower():
                    self.speech_engine.setProperty('voice', voice.id)
                    break
            
            # Set speech rate and volume
            self.speech_engine.setProperty('rate', 150)  # Speed of speech
            self.speech_engine.setProperty('volume', 0.9)  # Volume level
            
        except Exception as e:
            print(f"⚠️ Speech engine setup warning: {e}")
    
    def speak(self, text, block=True):
        """Convert text to speech"""
        try:
            if block:
                self.speech_engine.say(text)
                self.speech_engine.runAndWait()
            else:
                # Non-blocking speech in a separate thread
                def speak_thread():
                    self.speech_engine.say(text)
                    self.speech_engine.runAndWait()
                
                threading.Thread(target=speak_thread, daemon=True).start()
        except Exception as e:
            print(f"❌ Speech error: {e}")
    
    def search_applications(self, app_name):
        """Search for applications in common Windows locations"""
        app_name = app_name.lower()
        found_apps = []
        
        # Common Windows application paths
        search_paths = [
            os.path.expanduser("~\\AppData\\Local\\Microsoft\\WindowsApps"),
            "C:\\Program Files",
            "C:\\Program Files (x86)",
            os.path.expanduser("~\\AppData\\Local\\Programs"),
            os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"),
            "C:\\Windows\\System32"
        ]
        
        # Search in registry for installed applications
        try:
            registry_paths = [
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths"),
                (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths")
            ]
            
            for hkey, path in registry_paths:
                try:
                    with winreg.OpenKey(hkey, path) as key:
                        for i in range(winreg.QueryInfoKey(key)[0]):
                            try:
                                subkey_name = winreg.EnumKey(key, i)
                                if app_name in subkey_name.lower():
                                    try:
                                        with winreg.OpenKey(key, subkey_name) as subkey:
                                            try:
                                                exe_path, _ = winreg.QueryValueEx(subkey, "")
                                                if exe_path and os.path.exists(exe_path):
                                                    found_apps.append(exe_path)
                                            except:
                                                pass
                                    except:
                                        pass
                            except:
                                continue
                except:
                    continue
        except:
            pass
        
        # Search in file system
        for search_path in search_paths:
            if os.path.exists(search_path):
                try:
                    for root, dirs, files in os.walk(search_path):
                        for file in files:
                            if file.lower().endswith('.exe') and app_name in file.lower():
                                full_path = os.path.join(root, file)
                                if full_path not in found_apps:
                                    found_apps.append(full_path)
                except:
                    continue
        
        return found_apps

    def open_app_by_name(self, app_name):
        """Try to open app by name, searching system if not found"""
        try:
            # First try direct execution
            if platform.system() == "Windows":
                try:
                    subprocess.Popen(app_name)
                    success_msg = f"{app_name} opened successfully!"
                    print(f"✅ {success_msg}")
                    self.speak(success_msg, block=False)
                    return True
                except:
                    pass
            elif platform.system() == "Linux":
                try:
                    subprocess.Popen([app_name])
                    success_msg = f"{app_name} opened successfully!"
                    print(f"✅ {success_msg}")
                    self.speak(success_msg, block=False)
                    return True
                except:
                    pass
            elif platform.system() == "Darwin":
                try:
                    subprocess.Popen(["open", "-a", app_name])
                    success_msg = f"{app_name} opened successfully!"
                    print(f"✅ {success_msg}")
                    self.speak(success_msg, block=False)
                    return True
                except:
                    pass
            
            # If direct execution fails, search for the application
            search_msg = f"Searching for {app_name} in your system"
            print(f"🔍 {search_msg}...")
            self.speak(search_msg, block=False)
            
            found_apps = self.search_applications(app_name)
            
            if found_apps:
                # Try to open the first found application
                try:
                    subprocess.Popen(found_apps[0])
                    app_name_clean = os.path.basename(found_apps[0])
                    success_msg = f"Found and opened {app_name_clean}"
                    print(f"✅ {success_msg}")
                    self.speak(success_msg, block=False)
                    return True
                except Exception as e:
                    error_msg = f"Error opening {found_apps[0]}: {e}"
                    print(f"❌ {error_msg}")
                    self.speak("Sorry, there was an error opening the application", block=False)
                    return False
            else:
                not_found_msg = f"Could not find {app_name} in your system"
                print(f"❌ {not_found_msg}")
                self.speak(not_found_msg, block=False)
                return False
                
        except Exception as e:
            error_msg = f"Error: {e}"
            print(f"❌ {error_msg}")
            self.speak("Sorry, an error occurred", block=False)
            return False

    def process_command(self, command):
        """Process voice command and execute appropriate action"""
        command = command.lower()
        print(f"🧠 Aapne bola: {command}")

        # Check for exit commands
        if any(word in command for word in ["exit", "quit", "stop", "band karo", "band", "exit karo"]):
            goodbye_msg = "Goodbye! Voice assistant shutting down"
            print(f"👋 {goodbye_msg}...")
            self.speak(goodbye_msg)
            return False

        # Check for specific known apps first
        if "chrome" in command or "google chrome" in command:
            self.open_app_by_name("chrome.exe")
        elif "notepad" in command:
            self.open_app_by_name("notepad.exe")
        elif "calculator" in command or "calc" in command:
            self.open_app_by_name("calc.exe")
        elif "word" in command or "microsoft word" in command:
            self.open_app_by_name("winword.exe")
        elif "excel" in command or "microsoft excel" in command:
            self.open_app_by_name("excel.exe")
        elif "powerpoint" in command or "microsoft powerpoint" in command:
            self.open_app_by_name("powerpnt.exe")
        elif "paint" in command:
            self.open_app_by_name("mspaint.exe")
        elif "explorer" in command or "file explorer" in command:
            self.open_app_by_name("explorer.exe")
        elif "cmd" in command or "command prompt" in command:
            self.open_app_by_name("cmd.exe")
        elif "powershell" in command:
            self.open_app_by_name("powershell.exe")
        elif "help" in command or "help karo" in command:
            self.show_help()
        elif "hello" in command or "hi" in command or "namaste" in command:
            greeting_msg = "Hello! How can I help you today?"
            print(f"👋 {greeting_msg}")
            self.speak(greeting_msg, block=False)
        elif "how are you" in command or "kaise ho" in command:
            response_msg = "I'm doing great! Thank you for asking. How can I assist you?"
            print(f"😊 {response_msg}")
            self.speak(response_msg, block=False)
        elif "thank you" in command or "thanks" in command or "dhanyavad" in command:
            thanks_msg = "You're welcome! Is there anything else I can help you with?"
            print(f"🙏 {thanks_msg}")
            self.speak(thanks_msg, block=False)
        else:
            # Extract app name from command and search
            app_name = command.strip()
            if app_name:
                search_msg = f"Searching for {app_name}"
                print(f"🔍 {search_msg}")
                self.speak(search_msg, block=False)
                self.open_app_by_name(app_name)
            else:
                no_app_msg = "No app name detected in your command"
                print(f"❌ {no_app_msg}")
                self.speak(no_app_msg, block=False)
        
        return True

    def show_help(self):
        """Show available commands"""
        help_text = """
        Available Commands:
        Built-in apps: chrome, notepad, calculator, word, excel, powerpoint, paint, explorer, cmd, powershell
        Or say any app name to search your system!
        Say exit or quit to close the assistant
        Say help for this list
        """
        print("\n📋 Available Commands:")
        print("🎯 Built-in apps:")
        print("   - 'chrome' or 'google chrome'")
        print("   - 'notepad'")
        print("   - 'calculator' or 'calc'")
        print("   - 'word' or 'microsoft word'")
        print("   - 'excel' or 'microsoft excel'")
        print("   - 'powerpoint' or 'microsoft powerpoint'")
        print("   - 'paint'")
        print("   - 'explorer' or 'file explorer'")
        print("   - 'cmd' or 'command prompt'")
        print("   - 'powershell'")
        print("\n🔍 Or say any app name to search your system!")
        print("❌ Say 'exit' or 'quit' to close the assistant")
        print("❓ Say 'help' for this list\n")
        
        self.speak("Here are the available commands. You can say chrome, notepad, calculator, or any app name to open it. Say exit to quit.", block=False)

    def start(self):
        """Main voice assistant function with continuous operation"""
        print("🎤 Voice Assistant with Speech Started!")
        print("💡 Say 'help' for available commands")
        print("❌ Say 'exit' to quit\n")
        
        welcome_msg = "Hello! I'm your voice assistant. How can I help you today?"
        self.speak(welcome_msg)
        
        while True:
            try:
                with self.recognizer.Microphone() as source:
                    print("🎤 Listening... (Say 'exit' to quit)")
                    # Adjust for ambient noise
                    self.recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)

                command = self.recognizer.recognize_google(audio)
                
                # Process the command
                if not self.process_command(command):
                    break
                    
            except sr.WaitTimeoutError:
                timeout_msg = "No speech detected within timeout. Try again"
                print(f"⏰ {timeout_msg}...")
                self.speak(timeout_msg, block=False)
            except sr.UnknownValueError:
                unknown_msg = "Voice not understood. Try again"
                print(f"😕 {unknown_msg}...")
                self.speak(unknown_msg, block=False)
            except sr.RequestError as e:
                error_msg = f"Speech API error: {e}"
                print(f"🔌 {error_msg}")
                self.speak("Sorry, there was a problem with speech recognition", block=False)
            except KeyboardInterrupt:
                print("\n👋 Voice assistant stopped by user.")
                self.speak("Voice assistant stopped by user")
                break
            except Exception as e:
                error_msg = f"Unexpected error: {e}"
                print(f"❌ {error_msg}")
                self.speak("Sorry, an unexpected error occurred", block=False)
            
            print()  # Add spacing between commands

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.start() 