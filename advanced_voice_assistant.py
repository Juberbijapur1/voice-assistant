import speech_recognition as sr
import subprocess
import platform
import os
import winreg
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import time
import psutil
import threading

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

def close_app_by_name(app_name):
    """Close application by name"""
    try:
        app_name = app_name.lower()
        closed_count = 0
        
        # Common app name mappings
        app_mappings = {
            "chrome": ["chrome.exe", "google chrome"],
            "firefox": ["firefox.exe"],
            "edge": ["msedge.exe"],
            "notepad": ["notepad.exe"],
            "calculator": ["calc.exe"],
            "word": ["winword.exe"],
            "excel": ["excel.exe"],
            "powerpoint": ["powerpnt.exe"],
            "paint": ["mspaint.exe"],
            "explorer": ["explorer.exe"],
            "cmd": ["cmd.exe"],
            "powershell": ["powershell.exe"],
            "youtube": ["chrome.exe", "firefox.exe", "msedge.exe"],  # Close browser tabs
            "facebook": ["chrome.exe", "firefox.exe", "msedge.exe"],
            "twitter": ["chrome.exe", "firefox.exe", "msedge.exe"],
            "instagram": ["chrome.exe", "firefox.exe", "msedge.exe"],
            "gmail": ["chrome.exe", "firefox.exe", "msedge.exe"]
        }
        
        # Get processes to close
        processes_to_close = []
        if app_name in app_mappings:
            processes_to_close = app_mappings[app_name]
        else:
            # Try to find by partial name match
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if app_name in proc.info['name'].lower():
                        processes_to_close.append(proc.info['name'])
                except:
                    continue
        
        # Close processes
        for proc_name in processes_to_close:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'].lower() == proc_name.lower():
                        proc.terminate()
                        closed_count += 1
                        print(f"✅ Closed {proc.info['name']}")
                except:
                    continue
        
        if closed_count > 0:
            success_msg = f"Closed {closed_count} instance(s) of {app_name}"
            print(f"✅ {success_msg}")
            speak(success_msg)
            return True
        else:
            not_found_msg = f"No running instances of {app_name} found"
            print(f"❌ {not_found_msg}")
            speak(not_found_msg)
            return False
            
    except Exception as e:
        error_msg = f"Error closing {app_name}: {e}"
        print(f"❌ {error_msg}")
        speak("Sorry, there was an error closing the application")
        return False

def open_website(url):
    """Open a website in the default browser"""
    try:
        # Add https:// if not present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        webbrowser.open(url)
        success_msg = f"Opening {url}"
        print(f"🌐 {success_msg}")
        speak(success_msg)
        return True
    except Exception as e:
        error_msg = f"Error opening website: {e}"
        print(f"❌ {error_msg}")
        speak("Sorry, there was an error opening the website")
        return False

def web_search(query, search_type="general"):
    """Perform a web search with specific type"""
    try:
        if search_type == "video":
            # YouTube search
            search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
            success_msg = f"Searching YouTube for {query}"
        elif search_type == "image":
            # Google Images search
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=isch"
            success_msg = f"Searching images for {query}"
        elif search_type == "news":
            # Google News search
            search_url = f"https://news.google.com/search?q={urllib.parse.quote(query)}"
            success_msg = f"Searching news for {query}"
        elif search_type == "shopping":
            # Google Shopping search
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=shop"
            success_msg = f"Searching for products: {query}"
        else:
            # General Google search
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            success_msg = f"Searching the web for {query}"
        
        webbrowser.open(search_url)
        print(f"🔍 {success_msg}")
        speak(success_msg)
        return True
    except Exception as e:
        error_msg = f"Error performing web search: {e}"
        print(f"❌ {error_msg}")
        speak("Sorry, there was an error performing the web search")
        return False

def get_weather_info(city="current location"):
    """Get weather information for a city"""
    try:
        if city == "current location":
            city = "New York"
        
        # Using OpenWeatherMap API (free tier)
        api_key = "YOUR_API_KEY"  # Replace with your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            
            weather_msg = f"Weather in {city}: {temp}°C, {description}, humidity {humidity}%"
            print(f"🌤️ {weather_msg}")
            speak(weather_msg)
        else:
            # Fallback to web search
            web_search(f"weather in {city}")
            
    except Exception as e:
        print(f"❌ Weather error: {e}")
        # Fallback to web search
        web_search(f"weather in {city}")

def get_news():
    """Get latest news"""
    try:
        news_url = "https://news.google.com"
        webbrowser.open(news_url)
        success_msg = "Opening latest news"
        print(f"📰 {success_msg}")
        speak(success_msg)
        return True
    except Exception as e:
        error_msg = f"Error getting news: {e}"
        print(f"❌ {error_msg}")
        speak("Sorry, there was an error getting the news")
        return False

def get_time():
    """Get current time"""
    import datetime
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    time_msg = f"Current time is {current_time}"
    print(f"🕐 {time_msg}")
    speak(time_msg)

def get_date():
    """Get current date"""
    import datetime
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    date_msg = f"Today is {current_date}"
    print(f"📅 {date_msg}")
    speak(date_msg)

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

    # Close commands
    if command.startswith("close "):
        app_name = command.replace("close ", "").strip()
        if app_name:
            close_app_by_name(app_name)
        else:
            speak("What would you like me to close?")
        return True

    # Enhanced search commands
    if "search video" in command or "find video" in command:
        query = command.replace("search video", "").replace("find video", "").strip()
        if query:
            web_search(query, "video")
        else:
            speak("What video would you like me to search for?")
        return True
    
    elif "search image" in command or "find image" in command:
        query = command.replace("search image", "").replace("find image", "").strip()
        if query:
            web_search(query, "image")
        else:
            speak("What image would you like me to search for?")
        return True
    
    elif "search news" in command or "find news" in command:
        query = command.replace("search news", "").replace("find news", "").strip()
        if query:
            web_search(query, "news")
        else:
            get_news()
        return True
    
    elif "search shopping" in command or "find product" in command:
        query = command.replace("search shopping", "").replace("find product", "").strip()
        if query:
            web_search(query, "shopping")
        else:
            speak("What product would you like me to search for?")
        return True

    # Web-related commands
    if "search" in command or "google" in command:
        # Extract search query
        search_terms = ["search", "google", "find", "look for"]
        query = command
        for term in search_terms:
            query = query.replace(term, "").strip()
        if query:
            web_search(query)
        else:
            speak("What would you like me to search for?")
    
    elif "open website" in command or "go to" in command or "visit" in command:
        # Extract website URL
        website_terms = ["open website", "go to", "visit", "open"]
        url = command
        for term in website_terms:
            url = url.replace(term, "").strip()
        if url:
            open_website(url)
        else:
            speak("Which website would you like me to open?")
    
    elif "weather" in command:
        # Extract city name
        city = command.replace("weather", "").replace("in", "").strip()
        if city:
            get_weather_info(city)
        else:
            get_weather_info()
    
    elif "news" in command:
        get_news()
    
    elif "time" in command:
        get_time()
    
    elif "date" in command:
        get_date()
    
    elif "youtube" in command:
        if "search" in command:
            # Extract search query for YouTube
            query = command.replace("youtube", "").replace("search", "").strip()
            if query:
                web_search(query, "video")
            else:
                speak("What would you like me to search on YouTube?")
        else:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
    
    elif "facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    
    elif "twitter" in command or "x" in command:
        webbrowser.open("https://twitter.com")
        speak("Opening Twitter")
    
    elif "instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    
    elif "gmail" in command or "email" in command:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail")
    
    elif "maps" in command or "google maps" in command:
        webbrowser.open("https://maps.google.com")
        speak("Opening Google Maps")
    
    # Application commands
    elif "chrome" in command or "google chrome" in command:
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
    
    # General commands
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
        # Try to open as website first, then as app
        if "." in command or "www" in command:
            open_website(command)
        else:
            # Extract app name from command and search
            app_name = command.strip()
            if app_name:
                search_msg = f"Searching for {app_name}"
                print(f"🔍 {search_msg}")
                speak(search_msg)
                open_app_by_name(app_name)
            else:
                no_app_msg = "No command detected. Try saying 'help' for available commands"
                print(f"❌ {no_app_msg}")
                speak(no_app_msg)
    
    return True

def show_help():
    """Show available commands"""
    print("\n📋 Available Commands:")
    print("🔍 Enhanced Search:")
    print("   - 'search video [query]' - Search YouTube")
    print("   - 'search image [query]' - Search Google Images")
    print("   - 'search news [query]' - Search Google News")
    print("   - 'search shopping [query]' - Search Google Shopping")
    print("   - 'search [query]' or 'google [query]' - General search")
    print("\n🌐 Website Commands:")
    print("   - 'open youtube', 'go to facebook', 'visit gmail'")
    print("   - 'open maps', 'open twitter', 'open instagram'")
    print("\n❌ Close Commands:")
    print("   - 'close chrome', 'close notepad', 'close youtube'")
    print("   - 'close facebook', 'close gmail', 'close [app name]'")
    print("\n💻 App Commands:")
    print("   - 'chrome', 'notepad', 'calculator', 'word', 'excel'")
    print("   - 'paint', 'explorer', 'cmd', 'powershell'")
    print("\n📰 Information:")
    print("   - 'weather [city]', 'news', 'time', 'date'")
    print("\n❌ Say 'exit' or 'quit' to close the assistant")
    print("❓ Say 'help' for this list\n")
    
    speak("Here are the available commands. You can search for videos, images, news, close applications, open websites, and more. Say exit to quit.")

def voice_assistant():
    """Main voice assistant function with continuous operation"""
    r = sr.Recognizer()
    
    print("🎤 Advanced Voice Assistant Started!")
    print("💡 Say 'help' for available commands")
    print("❌ Say 'exit' to quit\n")
    
    welcome_msg = "Hello! I'm your advanced voice assistant. I can search the web, open and close applications, find videos, images, and more. How can I help you today?"
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