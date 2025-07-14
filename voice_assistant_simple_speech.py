import speech_recognition as sr
import subprocess
import platform
import os
import winreg
import pyttsx3

def speak(text):
    """Simple text-to-speech function"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.8)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")

def search_applications(app_name):
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

def open_app_by_name(app_name):
    """Try to open app by name, searching system if not found"""
    try:
        # First try direct execution
        if platform.system() == "Windows":
            try:
                subprocess.Popen(app_name)
                success_msg = f"{app_name} opened successfully!"
                print(f"✅ {success_msg}")
                speak(success_msg)
                return True
            except:
                pass
        elif platform.system() == "Linux":
            try:
                subprocess.Popen([app_name])
                success_msg = f"{app_name} opened successfully!"
                print(f"✅ {success_msg}")
                speak(success_msg)
                return True
            except:
                pass
        elif platform.system() == "Darwin":
            try:
                subprocess.Popen(["open", "-a", app_name])
                success_msg = f"{app_name} opened successfully!"
                print(f"✅ {success_msg}")
                speak(success_msg)
                return True
            except:
                pass
        
        # If direct execution fails, search for the application
        search_msg = f"Searching for {app_name} in your system"
        print(f"🔍 {search_msg}...")
        speak(search_msg)
        
        found_apps = search_applications(app_name)
        
        if found_apps:
            # Try to open the first found application
            try:
                subprocess.Popen(found_apps[0])
                app_name_clean = os.path.basename(found_apps[0])
                success_msg = f"Found and opened {app_name_clean}"
                print(f"✅ {success_msg}")
                speak(success_msg)
                return True
            except Exception as e:
                error_msg = f"Error opening {found_apps[0]}: {e}"
                print(f"❌ {error_msg}")
                speak("Sorry, there was an error opening the application")
                return False
        else:
            not_found_msg = f"Could not find {app_name} in your system"
            print(f"❌ {not_found_msg}")
            speak(not_found_msg)
            return False
            
    except Exception as e:
        error_msg = f"Error: {e}"
        print(f"❌ {error_msg}")
        speak("Sorry, an error occurred")
        return False

def process_command(command):
    """Process voice command and execute appropriate action"""
    command = command.lower()
    print(f"🧠 Aapne bola: {command}")

    # Check for exit commands
    if any(word in command for word in ["exit", "quit", "stop", "band karo", "band", "exit karo"]):
        goodbye_msg = "Goodbye! Voice assistant shutting down"
        print(f"👋 {goodbye_msg}...")
        speak(goodbye_msg)
        return False

    # Check for specific known apps first
    if "chrome" in command or "google chrome" in command:
        open_app_by_name("chrome.exe")
    elif "notepad" in command:
        open_app_by_name("notepad.exe")
    elif "calculator" in command or "calc" in command:
        open_app_by_name("calc.exe")
    elif "word" in command or "microsoft word" in command:
        open_app_by_name("winword.exe")
    elif "excel" in command or "microsoft excel" in command:
        open_app_by_name("excel.exe")
    elif "powerpoint" in command or "microsoft powerpoint" in command:
        open_app_by_name("powerpnt.exe")
    elif "paint" in command:
        open_app_by_name("mspaint.exe")
    elif "explorer" in command or "file explorer" in command:
        open_app_by_name("explorer.exe")
    elif "cmd" in command or "command prompt" in command:
        open_app_by_name("cmd.exe")
    elif "powershell" in command:
        open_app_by_name("powershell.exe")
    elif "help" in command or "help karo" in command:
        show_help()
    elif "hello" in command or "hi" in command or "namaste" in command:
        greeting_msg = "Hello! How can I help you today?"
        print(f"👋 {greeting_msg}")
        speak(greeting_msg)
    elif "how are you" in command or "kaise ho" in command:
        response_msg = "I'm doing great! Thank you for asking. How can I assist you?"
        print(f"😊 {response_msg}")
        speak(response_msg)
    elif "thank you" in command or "thanks" in command or "dhanyavad" in command:
        thanks_msg = "You're welcome! Is there anything else I can help you with?"
        print(f"🙏 {thanks_msg}")
        speak(thanks_msg)
    else:
        # Extract app name from command and search
        app_name = command.strip()
        if app_name:
            search_msg = f"Searching for {app_name}"
            print(f"🔍 {search_msg}")
            speak(search_msg)
            open_app_by_name(app_name)
        else:
            no_app_msg = "No app name detected in your command"
            print(f"❌ {no_app_msg}")
            speak(no_app_msg)
    
    return True

def show_help():
    """Show available commands"""
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
    
    speak("Here are the available commands. You can say chrome, notepad, calculator, or any app name to open it. Say exit to quit.")

def voice_assistant():
    """Main voice assistant function with continuous operation"""
    r = sr.Recognizer()
    
    print("🎤 Voice Assistant with Speech Started!")
    print("💡 Say 'help' for available commands")
    print("❌ Say 'exit' to quit\n")
    
    welcome_msg = "Hello! I'm your voice assistant. How can I help you today?"
    speak(welcome_msg)
    
    while True:
        try:
            with sr.Microphone() as source:
                print("🎤 Listening... (Say 'exit' to quit)")
                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=10)

            command = r.recognize_google(audio)
            
            # Process the command
            if not process_command(command):
                break
                
        except sr.WaitTimeoutError:
            timeout_msg = "No speech detected within timeout. Try again"
            print(f"⏰ {timeout_msg}...")
            speak(timeout_msg)
        except sr.UnknownValueError:
            unknown_msg = "Voice not understood. Try again"
            print(f"😕 {unknown_msg}...")
            speak(unknown_msg)
        except sr.RequestError as e:
            error_msg = f"Speech API error: {e}"
            print(f"🔌 {error_msg}")
            speak("Sorry, there was a problem with speech recognition")
        except KeyboardInterrupt:
            print("\n👋 Voice assistant stopped by user.")
            speak("Voice assistant stopped by user")
            break
        except Exception as e:
            error_msg = f"Unexpected error: {e}"
            print(f"❌ {error_msg}")
            speak("Sorry, an unexpected error occurred")
        
        print()  # Add spacing between commands

if __name__ == "__main__":
    voice_assistant() 