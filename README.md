# Voice Assistant

A simple voice-controlled application launcher that can open applications using voice commands.

## Features

- 🎤 Voice recognition using Google Speech Recognition API
- 💻 Cross-platform support (Windows, Linux, macOS)
- 🚀 Opens applications based on voice commands
- 🌐 Hindi/Urdu interface

## Supported Commands

Currently supports opening these applications:
- **Chrome** - Say "chrome" to open Google Chrome
- **Notepad** - Say "notepad" to open Notepad
- **Calculator** - Say "calculator" to open Calculator

## Prerequisites

- Python 3.7 or higher
- Working microphone
- Internet connection (for Google Speech Recognition API)

## Installation

### Option 1: Automatic Setup (Recommended)
```bash
python setup.py
```

### Option 2: Manual Setup
```bash
pip install -r requirements.txt
```

## Usage

### Basic Version
1. Run the original voice assistant:
   ```bash
   python voice_model.py
   ```

2. When prompted "🎤 Boliye kis app ko open karna hai...", speak one of the supported commands:
   - "chrome"
   - "notepad" 
   - "calculator"

3. The application will open automatically if recognized.

### Enhanced Version (Recommended)
1. Run the enhanced voice assistant:
   ```bash
   python voice_assistant_enhanced.py
   ```

2. The assistant will start listening continuously. You can say:
   - **Built-in apps**: "chrome", "notepad", "calculator", "word", "excel", etc.
   - **Any app name**: "spotify", "discord", "steam", "code" (VS Code), etc.
   - **Help**: "help" to see all available commands
   - **Exit**: "exit" to close the assistant

3. The assistant will search your system and open the application if found.

### Web-Enabled Version
1. Run the web-enabled voice assistant:
   ```bash
   python web_voice_assistant.py
   ```

2. The assistant will start listening continuously. You can say:
   - **Web Search**: "search Python tutorial", "google latest news"
   - **Websites**: "open youtube", "go to facebook", "visit gmail"
   - **Information**: "what time is it", "get news", "weather in London"
   - **Applications**: "open chrome", "open notepad", etc.
   - **Help**: "help" to see all available commands
   - **Exit**: "exit" to close the assistant

3. The assistant will open websites, perform searches, and run applications.

### Advanced Version
1. Run the advanced voice assistant:
   ```bash
   python advanced_voice_assistant.py
   ```

2. The assistant will start listening continuously. You can say:
   - **Enhanced Search**: "search video Python tutorial", "search image sunset"
   - **Close Commands**: "close chrome", "close youtube", "close notepad"
   - **Websites**: "open youtube", "go to facebook", "visit gmail"
   - **Information**: "what time is it", "get news", "weather in London"
   - **Applications**: "open chrome", "open notepad", etc.
   - **Help**: "help" to see all available commands
   - **Exit**: "exit" to close the assistant

3. The assistant will open/close applications, perform specific searches, and manage your system.

### Media Version (Most Advanced)
1. Run the media voice assistant:
   ```bash
   python media_voice_assistant.py
   ```

2. The assistant will start listening continuously. You can say:
   - **Play Commands**: "play hamari kahani on youtube", "play shape of you on spotify"
   - **Video Commands**: "play avengers on netflix", "play game of thrones on prime"
   - **Artist Commands**: "play arijit singh on spotify", "play ed sheeran on youtube"
   - **All Previous Features**: Search, close apps, open websites, etc.
   - **Help**: "help" to see all available commands
   - **Exit**: "exit" to close the assistant

3. The assistant will open platforms and search for your requested content.

### Enhanced Version (NEW - RECOMMENDED)
1. Run the enhanced voice assistant:
   ```bash
   python enhanced_demo.py
   ```

2. The assistant will start listening continuously. You can say:
   - **Code Editors**: "open vs code", "open cursor", "open notepad"
   - **HTML Creation**: "create html personal portfolio", "make html business website"
   - **Math Solving**: "solve math 5 plus 3", "calculate 10 times 5"
   - **Interactive**: "hey partner" (anytime), "time", "date"
   - **Background Listening**: Assistant responds to "hey partner" during tasks
   - **Stop**: "stop" to close the assistant

3. The assistant will open code editors, create HTML files, solve math problems, and respond to your voice anytime.

### GUI Version (NEW - EASIEST TO USE)
1. Run the GUI voice assistant:
   ```bash
   python launch_gui.py
   ```

2. The GUI provides:
   - **Visual Interface**: Buttons and controls for easy operation
   - **Quick Actions**: Instant buttons for common tasks (VS Code, Notepad, HTML, Math, Time)
   - **Activity Log**: Real-time display of all actions and responses
   - **Start/Stop Controls**: Easy voice listening control
   - **Voice Commands Help**: Built-in command reference
   - **Status Indicators**: Visual feedback of current state

3. Click "Start Listening" to begin voice recognition, then use voice commands or quick action buttons.

### Test Functionality
To test the search capabilities:
```bash
python test_search.py
```

To see web capabilities demo:
```bash
python web_demo.py
```

To see advanced features demo:
```bash
python advanced_demo.py
```

To see media features demo:
```bash
python media_demo.py
```

To test enhanced voice assistant setup:
```bash
python test_enhanced_setup.py
```

To launch the GUI version:
```bash
python launch_gui.py
```

To see GUI demo:
```bash
python gui_demo.py
```

## Troubleshooting

### Microphone Issues
- Ensure your microphone is connected and working
- Check Windows microphone permissions
- Try running as administrator if needed

### PyAudio Installation Issues (Windows)
If you get errors installing PyAudio on Windows, try:
```bash
pip install pipwin
pipwin install pyaudio
```

### Speech Recognition Issues
- Check your internet connection
- Ensure you're speaking clearly
- Try speaking in English if Hindi/Urdu isn't working

## Enhanced Features

### 🔍 **System-Wide Application Search**
- Searches Windows Registry for installed applications
- Scans common installation directories
- Finds applications even if not in PATH
- Supports any application name you speak

### 🎯 **Built-in Commands**
- **Chrome**: "chrome" or "google chrome"
- **Notepad**: "notepad"
- **Calculator**: "calculator" or "calc"
- **Microsoft Office**: "word", "excel", "powerpoint"
- **System Tools**: "paint", "explorer", "cmd", "powershell"
- **Help**: "help" or "help karo"
- **Exit**: "exit", "quit", "stop", "band karo"

### 🔄 **Continuous Operation**
- Runs continuously until you say "exit"
- Better error handling and feedback
- Ambient noise adjustment
- Timeout handling

## Web-Enabled Features

### 🌐 **Web Search & Navigation**
- **Google Search**: "search Python tutorial" or "google latest news"
- **Website Opening**: "open youtube", "go to facebook", "visit gmail"
- **Social Media**: "open twitter", "go to instagram", "open facebook"
- **Email & Maps**: "open gmail", "open maps"

### 📰 **Information & News**
- **News**: "get news" - Opens Google News
- **Weather**: "weather in London" - Get weather information
- **Time & Date**: "what time is it", "what's the date today"

### 🎯 **Smart Commands**
- **YouTube**: "open youtube" or "youtube search [query]"
- **Maps**: "open maps" or "google maps"
- **Email**: "open gmail" or "gmail"

## Advanced Features

### ❌ **App & Website Closing**
- **Close Applications**: "close chrome", "close notepad", "close calculator"
- **Close Websites**: "close youtube", "close facebook", "close gmail"
- **Smart Process Management**: Automatically finds and closes running processes

### 🔍 **Enhanced Search Types**
- **Video Search**: "search video Python tutorial" → YouTube search
- **Image Search**: "search image sunset" → Google Images search
- **News Search**: "search news technology" → Google News search
- **Shopping Search**: "search shopping laptops" → Google Shopping search
- **General Search**: "search Python programming" → Google search

### 🎯 **Smart Commands**
- **YouTube**: "youtube search funny cats" → Direct YouTube search
- **Specific Content**: "find video music videos", "search image cute puppies"
- **Product Search**: "find product smartphones" → Shopping search

## Media Features

### 🎵 **Play Commands**
- **Music Platforms**: "play hamari kahani on youtube", "play shape of you on spotify"
- **Video Platforms**: "play avengers on netflix", "play game of thrones on prime"
- **Artist Search**: "play arijit singh on spotify", "play ed sheeran on youtube"
- **Genre Search**: "play bollywood on youtube", "play rock music on spotify"

### 🌐 **Supported Platforms**
- **Music**: YouTube, Spotify, Apple Music, Amazon Music, Deezer, SoundCloud
- **Video**: Netflix, Amazon Prime, Disney+, Hulu
- **General**: Any website with search functionality

### 🎯 **Smart Recognition**
- **Pattern**: "play [content] on [platform]"
- **Examples**: "play hamari kahani on youtube", "play shape of you on spotify"
- **Fallback**: If no platform specified, defaults to YouTube

## Enhanced Features (NEW)

### 💻 **Code Editor Integration**
- **VS Code**: "open vs code" - Opens Visual Studio Code
- **Cursor**: "open cursor" - Opens Cursor editor
- **Notepad**: "open notepad" - Opens Notepad
- **Any Editor**: "open [editor name]" - Searches and opens any code editor

### 🌐 **HTML Code Generation**
- **Voice to HTML**: "create html personal portfolio" - Generates HTML file
- **Template Creation**: "make html business website" - Creates styled HTML
- **Custom Pages**: "generate html blog page" - Creates HTML templates
- **Auto-save**: Files saved with timestamp for easy identification

### 🧮 **Mathematical Problem Solving**
- **Basic Math**: "solve math 5 plus 3" - Calculates 5 + 3
- **Complex Operations**: "calculate 10 times 5" - Calculates 10 * 5
- **Division**: "solve math 100 divided by 4" - Calculates 100 / 4
- **Safe Evaluation**: Only allows basic mathematical operations

### 🎤 **Interactive Voice Response**
- **Background Listening**: "hey partner" - Gets attention anytime
- **Task Interruption**: Responds during ongoing tasks
- **Voice Feedback**: Speaks all responses and confirmations
- **Continuous Operation**: Runs until you say "stop"

### ⏰ **Time & Information**
- **Current Time**: "time" - Tells current time
- **Current Date**: "date" - Tells current date
- **Voice Announcements**: All information spoken aloud

## GUI Features (NEW)

### 🖥️ **Visual Interface**
- **Start/Stop Controls**: Easy buttons to control voice listening
- **Quick Action Buttons**: Instant access to common tasks
- **Activity Log**: Real-time display of all actions and responses
- **Status Indicators**: Visual feedback of current state
- **Voice Commands Help**: Built-in command reference

### 🎯 **Quick Actions**
- **💻 Open VS Code**: Instant button to launch Visual Studio Code
- **📝 Open Notepad**: Quick access to Notepad editor
- **🌐 Create HTML**: Generates sample HTML file instantly
- **🧮 Solve Math**: Calculates 5 + 3 with one click
- **⏰ Get Time**: Shows current time immediately

### 📊 **Real-time Feedback**
- **Activity Log**: All voice commands and responses displayed
- **Timestamped Entries**: Every action logged with time
- **Scrollable History**: View all previous interactions
- **Clear Log**: Easy button to clear activity history

## File Structure

```
voice assistant/
├── voice_model.py                    # Original voice assistant script
├── voice_assistant_enhanced.py       # Enhanced version with search
├── voice_assistant_simple_speech.py  # Version with speech output
├── web_voice_assistant.py            # Web-enabled version
├── advanced_voice_assistant.py       # Advanced version
├── media_voice_assistant.py          # Media version
├── enhanced_voice_assistant.py       # Enhanced version (NEW - RECOMMENDED)
├── enhanced_demo.py                  # Demo of enhanced features
├── voice_assistant_gui.py            # GUI version (NEW - EASIEST TO USE)
├── launch_gui.py                     # GUI launcher with error handling
├── gui_demo.py                       # GUI demo and information
├── test_enhanced_setup.py            # Test enhanced setup
├── requirements_enhanced.txt         # Enhanced dependencies
├── test_search.py                    # Test script for search functionality
├── web_demo.py                       # Demo of web capabilities
├── advanced_demo.py                  # Demo of advanced features
├── media_demo.py                     # Demo of media features
├── requirements.txt                  # Python dependencies
├── setup.py                          # Setup script
└── README.md                         # This file
```

## Customization

To add more applications, modify the `recognize_and_open()` function in `voice_model.py`:

```python
elif "your_app" in command:
    open_app_by_name("your_app.exe")
```

## License

This project is open source and available under the MIT License. 