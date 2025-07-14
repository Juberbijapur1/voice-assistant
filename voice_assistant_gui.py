import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import speech_recognition as sr
import subprocess
import platform
import os
import winreg
import re
import math
import time
from pathlib import Path
import pyttsx3
from datetime import datetime
import webbrowser
import psutil

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Voice Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize voice assistant components
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
        
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the GUI components"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky='nsew')
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🎤 Enhanced Voice Assistant", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.grid(row=1, column=0, columnspan=3, sticky='ew', pady=(0, 10))
        
        self.status_label = ttk.Label(status_frame, text="Ready to listen", 
                                     font=('Arial', 10))
        self.status_label.grid(row=0, column=0, sticky=tk.W)
        
        # Control buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, sticky='nsew', padx=(0, 10))
        
        # Main control buttons
        self.start_button = ttk.Button(button_frame, text="🎤 Start Listening", 
                                      command=self.start_listening, style='Accent.TButton')
        self.start_button.grid(row=0, column=0, pady=5, sticky='ew')
        
        self.stop_button = ttk.Button(button_frame, text="⏹️ Stop Listening", 
                                     command=self.stop_listening, state='disabled')
        self.stop_button.grid(row=1, column=0, pady=5, sticky='ew')
        
        self.clear_button = ttk.Button(button_frame, text="🗑️ Clear Log", 
                                      command=self.clear_log)
        self.clear_button.grid(row=2, column=0, pady=5, sticky='ew')
        
        # Quick action buttons
        quick_frame = ttk.LabelFrame(button_frame, text="Quick Actions", padding="10")
        quick_frame.grid(row=3, column=0, pady=(20, 0), sticky='ew')
        
        ttk.Button(quick_frame, text="💻 Open VS Code", 
                  command=lambda: self.quick_action("open vs code")).grid(row=0, column=0, pady=2, sticky='ew')
        
        ttk.Button(quick_frame, text="📝 Open Notepad", 
                  command=lambda: self.quick_action("open notepad")).grid(row=1, column=0, pady=2, sticky='ew')
        
        ttk.Button(quick_frame, text="🌐 Create HTML", 
                  command=lambda: self.quick_action("create html sample page")).grid(row=2, column=0, pady=2, sticky='ew')
        
        ttk.Button(quick_frame, text="🧮 Solve Math", 
                  command=lambda: self.quick_action("solve math 5 plus 3")).grid(row=3, column=0, pady=2, sticky='ew')
        
        ttk.Button(quick_frame, text="⏰ Get Time", 
                  command=lambda: self.quick_action("time")).grid(row=4, column=0, pady=2, sticky='ew')
        
        # Log frame
        log_frame = ttk.LabelFrame(main_frame, text="Activity Log", padding="10")
        log_frame.grid(row=2, column=1, sticky='nsew')
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=20, width=60, 
                                                font=('Consolas', 9))
        self.log_text.grid(row=0, column=0, sticky='nsew')
        
        # Configure log frame grid weights
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        # Help frame
        help_frame = ttk.LabelFrame(main_frame, text="Voice Commands", padding="10")
        help_frame.grid(row=3, column=0, columnspan=3, sticky='ew', pady=(10, 0))
        
        help_text = """
🎯 Code Editors: "open vs code", "open cursor", "open notepad"
🌐 HTML Creation: "create html personal portfolio", "make html business website"
🧮 Math Solving: "solve math 5 plus 3", "calculate 10 times 5"
⏰ Information: "time", "date"
🎤 Interactive: "hey partner" (anytime)
⏹️ Stop: "stop" or "stop listening"
        """
        
        help_label = ttk.Label(help_frame, text=help_text, font=('Arial', 9))
        help_label.grid(row=0, column=0, sticky='w')
        
    def log_message(self, message):
        """Add message to log with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def update_status(self, status):
        """Update status label"""
        self.status_label.config(text=status)
        self.root.update_idletasks()
        
    def speak(self, text):
        """Convert text to speech and log it"""
        self.log_message(f"🤖 Assistant: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            self.log_message(f"❌ Speech error: {e}")
        
    def quick_action(self, command):
        """Execute a quick action from button"""
        self.log_message(f"🎯 Quick Action: {command}")
        self.process_command(command)
        
    def start_listening(self):
        """Start voice listening"""
        if not self.is_listening:
            self.is_listening = True
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')
            self.update_status("Listening for voice commands...")
            self.log_message("🎤 Voice assistant started")
            self.speak("Voice assistant is ready! Say 'hey partner' anytime.")
            
            # Start listening thread
            self.listen_thread = threading.Thread(target=self.listen_loop, daemon=True)
            self.listen_thread.start()
            
    def stop_listening(self):
        """Stop voice listening"""
        if self.is_listening:
            self.is_listening = False
            self.start_button.config(state='normal')
            self.stop_button.config(state='disabled')
            self.update_status("Stopped")
            self.log_message("⏹️ Voice assistant stopped")
            self.speak("Voice assistant stopped.")
            
    def clear_log(self):
        """Clear the activity log"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("🗑️ Log cleared")
        
    def listen_loop(self):
        """Main listening loop"""
        while self.is_listening:
            try:
                with sr.Microphone() as source:
                    self.r.adjust_for_ambient_noise(source, duration=1)
                    audio = self.r.listen(source, timeout=5, phrase_time_limit=10)
                
                try:
                    command = self.r.recognize_google(audio).lower()
                    self.log_message(f"🧠 You said: {command}")
                    
                    if not self.process_command(command):
                        break
                        
                except sr.UnknownValueError:
                    pass  # Don't log every unrecognized audio
                except sr.RequestError:
                    self.log_message("🔌 Speech API request failed.")
                    
            except sr.WaitTimeoutError:
                continue
            except Exception as e:
                self.log_message(f"❌ Listening error: {e}")
                break
        
        # Reset GUI when listening stops
        self.root.after(0, self.reset_gui)
        
    def reset_gui(self):
        """Reset GUI to initial state"""
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.update_status("Ready to listen")
        
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
    
    def close_app_by_name(self, app_name):
        """Close an application by process name (Windows)"""
        closed = False
        app_name = app_name.lower().replace('.exe', '')
        for proc in psutil.process_iter(['name']):
            try:
                pname = proc.info['name'].lower()
                if app_name in pname:
                    proc.terminate()
                    closed = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        if closed:
            self.speak(f"Closed all processes matching {app_name}.")
        else:
            self.speak(f"No running process found for {app_name}.")
        return closed

    def play_youtube_song(self, query):
        """Open YouTube search for the given song/query"""
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(url)
        self.speak(f"Playing {query} on YouTube.")

    def web_search(self, query, search_type=None):
        """Perform a web search (general, video, image, news, shopping)"""
        base = "https://www.google.com/search?q="
        if search_type == 'video':
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        elif search_type == 'image':
            url = f"{base}{query.replace(' ', '+')}&tbm=isch"
        elif search_type == 'news':
            url = f"{base}{query.replace(' ', '+')}&tbm=nws"
        elif search_type == 'shopping':
            url = f"{base}{query.replace(' ', '+')}&tbm=shop"
        else:
            url = f"{base}{query.replace(' ', '+')}"
        webbrowser.open(url)
        self.speak(f"Searching for {query} {search_type or ''}.")

    def play_on_platform(self, content, platform):
        """Play content on a specific platform (YouTube, Spotify, etc.)"""
        platform = platform.lower()
        if 'youtube' in platform:
            self.play_youtube_song(content)
        elif 'spotify' in platform:
            url = f"https://open.spotify.com/search/{content.replace(' ', '%20')}"
            webbrowser.open(url)
            self.speak(f"Playing {content} on Spotify.")
        elif 'netflix' in platform:
            url = f"https://www.netflix.com/search?q={content.replace(' ', '%20')}"
            webbrowser.open(url)
            self.speak(f"Searching for {content} on Netflix.")
        elif 'prime' in platform or 'amazon' in platform:
            url = f"https://www.amazon.com/s?k={content.replace(' ', '+')}"
            webbrowser.open(url)
            self.speak(f"Searching for {content} on Amazon Prime.")
        else:
            self.speak(f"Platform {platform} not supported. Playing on YouTube instead.")
            self.play_youtube_song(content)

    def process_command(self, command):
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
        
        # Close app command
        if command.startswith("close "):
            app_name = command.replace("close", "").strip()
            if app_name:
                self.close_app_by_name(app_name)
            else:
                self.speak("Please specify which app to close.")
        # Play song on YouTube
        elif command.startswith("play ") and " on youtube" in command:
            content = command.replace("play", "").replace("on youtube", "").strip()
            if content:
                self.play_youtube_song(content)
            else:
                self.speak("Please specify what to play on YouTube.")
        # Play on platform (YouTube, Spotify, etc.)
        elif command.startswith("play ") and " on " in command:
            parts = command.split(" on ")
            content = parts[0].replace("play", "").strip()
            platform = parts[1].strip()
            if content and platform:
                self.play_on_platform(content, platform)
            else:
                self.speak("Please specify what to play and on which platform.")
        # Web/media search commands
        elif command.startswith("search video "):
            query = command.replace("search video", "").strip()
            self.web_search(query, search_type='video')
        elif command.startswith("search image "):
            query = command.replace("search image", "").strip()
            self.web_search(query, search_type='image')
        elif command.startswith("search news "):
            query = command.replace("search news", "").strip()
            self.web_search(query, search_type='news')
        elif command.startswith("search shopping "):
            query = command.replace("search shopping", "").strip()
            self.web_search(query, search_type='shopping')
        elif command.startswith("search "):
            query = command.replace("search", "").strip()
            self.web_search(query)
        
        # Time and date
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today's date is {current_date}")
        
        # Stop listening
        elif "stop listening" in command or "stop" in command:
            self.stop_listening()
            return False
        
        # Hey partner
        elif "hey partner" in command or "hello partner" in command:
            self.speak("Hello! I'm here. What can I help you with?")
        
        else:
            self.speak("I didn't understand that command. Please try again.")
        
        return True

def main():
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    
    # Handle window close
    def on_closing():
        if app.is_listening:
            app.stop_listening()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 