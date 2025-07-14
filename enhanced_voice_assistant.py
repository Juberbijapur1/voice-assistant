import speech_recognition as sr
import subprocess
import platform
import os
import winreg
import glob
import re
import math
import threading
import time
from pathlib import Path
import pyttsx3
from datetime import datetime

class EnhancedVoiceAssistant:
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.is_listening = False
        self.current_task = None
        self.task_thread = None
        
        # Configure text-to-speech
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        # Get available voices and set to a good one
        try:
            voices = self.engine.getProperty('voices')
            if voices and hasattr(voices, '__len__') and len(voices) > 0:
                self.engine.setProperty('voice', voices[0].id)
        except:
            pass
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"🤖 Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
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
                    self.speak(f"{app_name} opened successfully!")
                    return True
                except:
                    pass
            elif platform.system() == "Linux":
                try:
                    subprocess.Popen([app_name])
                    self.speak(f"{app_name} opened successfully!")
                    return True
                except:
                    pass
            elif platform.system() == "Darwin":
                try:
                    subprocess.Popen(["open", "-a", app_name])
                    self.speak(f"{app_name} opened successfully!")
                    return True
                except:
                    pass
            
            # If direct execution fails, search for the application
            self.speak(f"Searching for {app_name} in your system...")
            found_apps = self.search_applications(app_name)
            
            if found_apps:
                # Try to open the first found application
                try:
                    subprocess.Popen(found_apps[0])
                    self.speak(f"Found and opened: {os.path.basename(found_apps[0])}")
                    return True
                except Exception as e:
                    self.speak(f"Error opening {found_apps[0]}: {e}")
                    return False
            else:
                self.speak(f"Could not find {app_name} in your system.")
                return False
                
        except Exception as e:
            self.speak(f"Error: {e}")
            return False
    
    def solve_math_problem(self, expression):
        """Solve mathematical expressions safely"""
        try:
            # Clean the expression - remove words and keep only math symbols
            expression = re.sub(r'[a-zA-Z\s]', '', expression)
            expression = expression.replace('plus', '+').replace('minus', '-').replace('times', '*').replace('divided by', '/')
            
            # Only allow safe mathematical operations
            allowed_chars = set('0123456789+-*/(). ')
            if not all(c in allowed_chars for c in expression):
                self.speak("Sorry, I can only solve basic mathematical expressions.")
                return None
            
            # Evaluate the expression
            result = eval(expression)
            return result
        except Exception as e:
            self.speak(f"Sorry, I couldn't solve that math problem: {e}")
            return None
    
    def create_html_code(self, description):
        """Create HTML code based on voice description"""
        try:
            # Create a simple HTML template based on the description
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{description.title()}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            text-align: center;
        }}
        p {{
            line-height: 1.6;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{description.title()}</h1>
        <p>This is a sample HTML page created based on your description: "{description}"</p>
        <p>You can modify this code to add more content and styling.</p>
    </div>
</body>
</html>"""
            
            # Save the HTML file
            filename = f"generated_{int(time.time())}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.speak(f"HTML file created successfully: {filename}")
            return filename
        except Exception as e:
            self.speak(f"Error creating HTML file: {e}")
            return None
    
    def listen_for_partner(self):
        """Listen for 'hey partner' during task execution"""
        while self.is_listening:
            try:
                with sr.Microphone() as source:
                    self.r.adjust_for_ambient_noise(source, duration=1)
                    audio = self.r.listen(source, timeout=1, phrase_time_limit=3)
                
                try:
                    command = self.r.recognize_google(audio).lower()
                    if "hey partner" in command or "hello partner" in command:
                        self.speak("Hello! I'm here. What can I help you with?")
                    elif "stop listening" in command or "stop" in command:
                        self.is_listening = False
                        self.speak("Stopping voice assistant.")
                        break
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    pass
            except:
                pass
    
    def execute_task(self, task_type, task_data):
        """Execute a task in a separate thread"""
        self.current_task = task_type
        self.speak(f"Starting {task_type} task...")
        
        if task_type == "html_creation":
            filename = self.create_html_code(task_data)
            if filename:
                self.speak("HTML file has been created and saved!")
        elif task_type == "math_solving":
            result = self.solve_math_problem(task_data)
            if result is not None:
                self.speak(f"The answer is: {result}")
        elif task_type == "app_opening":
            self.open_app_by_name(task_data)
        
        self.current_task = None
        self.speak("Task completed!")
    
    def process_command(self, command):
        """Process voice commands"""
        command = command.lower()
        
        # Code editor commands
        if "open" in command and ("vs code" in command or "visual studio code" in command):
            self.open_app_by_name("code.exe")
        elif "open" in command and "cursor" in command:
            self.open_app_by_name("cursor.exe")
        elif "open" in command and "notepad" in command:
            self.open_app_by_name("notepad.exe")
        
        # HTML creation commands
        elif "create html" in command or "make html" in command or "generate html" in command:
            # Extract the description after "create html"
            description = command.replace("create html", "").replace("make html", "").replace("generate html", "").strip()
            if description:
                self.task_thread = threading.Thread(target=self.execute_task, args=("html_creation", description))
                self.task_thread.start()
            else:
                self.speak("Please describe what kind of HTML page you want me to create.")
        
        # Math solving commands
        elif "solve" in command and ("math" in command or "calculate" in command):
            # Extract the math expression
            expression = command.replace("solve", "").replace("math", "").replace("calculate", "").strip()
            if expression:
                self.task_thread = threading.Thread(target=self.execute_task, args=("math_solving", expression))
                self.task_thread.start()
            else:
                self.speak("Please provide a mathematical expression to solve.")
        
        # App opening commands
        elif "open" in command:
            # Extract app name after "open"
            app_name = command.replace("open", "").strip()
            if app_name:
                self.task_thread = threading.Thread(target=self.execute_task, args=("app_opening", app_name))
                self.task_thread.start()
        
        # Time and date
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today's date is {current_date}")
        
        # Stop listening
        elif "stop listening" in command or "stop" in command:
            self.is_listening = False
            self.speak("Stopping voice assistant.")
            return False
        
        else:
            self.speak("I didn't understand that command. Please try again.")
        
        return True
    
    def run(self):
        """Main run loop"""
        self.speak("Enhanced Voice Assistant is ready! Say 'hey partner' anytime to get my attention.")
        self.is_listening = True
        
        # Start listening for "hey partner" in background
        partner_thread = threading.Thread(target=self.listen_for_partner)
        partner_thread.daemon = True
        partner_thread.start()
        
        while self.is_listening:
            try:
                with sr.Microphone() as source:
                    print("\n🎤 Listening for commands...")
                    print("💡 Say: 'open vs code', 'create html page', 'solve math 5 plus 3', 'time', etc.")
                    audio = self.r.listen(source, timeout=5, phrase_time_limit=10)
                
                try:
                    command = self.r.recognize_google(audio).lower()
                    print(f"🧠 You said: {command}")
                    
                    if not self.process_command(command):
                        break
                        
                except sr.UnknownValueError:
                    print("😕 Voice not understood.")
                except sr.RequestError:
                    print("🔌 Speech API request failed.")
                    
            except sr.WaitTimeoutError:
                continue
            except KeyboardInterrupt:
                break
        
        self.speak("Goodbye!")

if __name__ == "__main__":
    assistant = EnhancedVoiceAssistant()
    assistant.run() 