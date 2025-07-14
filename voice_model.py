import speech_recognition as sr
import subprocess
import platform
import os
import winreg
import glob
from pathlib import Path

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
                print(f"✅ {app_name} opened successfully!")
                return True
            except:
                pass
        elif platform.system() == "Linux":
            try:
                subprocess.Popen([app_name])
                print(f"✅ {app_name} opened successfully!")
                return True
            except:
                pass
        elif platform.system() == "Darwin":
            try:
                subprocess.Popen(["open", "-a", app_name])
                print(f"✅ {app_name} opened successfully!")
                return True
            except:
                pass
        
        # If direct execution fails, search for the application
        print(f"🔍 Searching for {app_name} in your system...")
        found_apps = search_applications(app_name)
        
        if found_apps:
            # Try to open the first found application
            try:
                subprocess.Popen(found_apps[0])
                print(f"✅ Found and opened: {os.path.basename(found_apps[0])}")
                return True
            except Exception as e:
                print(f"❌ Error opening {found_apps[0]}: {e}")
                return False
        else:
            print(f"❌ Could not find {app_name} in your system.")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def recognize_and_open():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Boliye kis app ko open karna hai...")
        print("💡 You can say: chrome, notepad, calculator, or any app name")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print(f"🧠 Aapne bola: {command}")

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
        else:
            # Extract app name from command and search
            app_name = command.strip()
            if app_name:
                print(f"🔍 Searching for: {app_name}")
                open_app_by_name(app_name)
            else:
                print("❌ No app name detected in your command.")

    except sr.UnknownValueError:
        print("😕 Voice samajh nahi aayi.")
    except sr.RequestError:
        print("🔌 Speech API ka request fail hua.")

# Run once
recognize_and_open()
