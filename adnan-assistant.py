import pyttsx3
import os
import webbrowser
import pyautogui
import datetime
import urllib.request
import shutil
import sys
import filecmp

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Ad.nan:", text)
    engine.say(text)
    engine.runAndWait()

def introduce():
    speak("Hello, I'm Ad.nan, your AI assistant. How can I help you today?")

def open_site(site):
    urls = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "whatsapp": "https://web.whatsapp.com"
    }
    if site in urls:
        speak(f"Opening {site}")
        webbrowser.open(urls[site])
    else:
        speak("I don't know that site.")

def control_system(command):
    if command == "shutdown":
        speak("Shutting down now.")
        os.system("shutdown /s /f /t 0")
    elif command == "restart":
        speak("Restarting system.")
        os.system("shutdown /r /f /t 0")

def mouse_action(action):
    if action == "click":
        pyautogui.click()
        speak("Mouse clicked.")
    elif action == "right click":
        pyautogui.rightClick()
        speak("Right clicked.")
    elif action == "move up":
        pyautogui.move(0, -100)
        speak("Mouse moved up.")
    elif action == "scroll up":
        pyautogui.scroll(500)
        speak("Scrolled up.")
    elif action == "scroll down":
        pyautogui.scroll(-500)
        speak("Scrolled down.")
    else:
        speak("Unknown mouse action.")

def window_control(action):
    if action == "minimize":
        pyautogui.hotkey("win", "d")
        speak("Minimizing all windows.")
    elif action == "maximize":
        pyautogui.hotkey("win", "up")
        speak("Maximizing window.")
    elif action == "close":
        pyautogui.hotkey("alt", "f4")
        speak("Closing window.")

def answer(question):
    if "time" in question:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif "date" in question:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    else:
        speak("Sorry, I don't have an answer for that.")

def update_self():
    try:
        # 🔁 Replace this with your GitHub raw link after uploading the file
        update_url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/adnan_assistant.py"
        local_path = os.path.realpath(__file__)
        new_path = local_path + ".new"

        urllib.request.urlretrieve(update_url, new_path)

        if not filecmp.cmp(local_path, new_path, shallow=False):
            shutil.move(new_path, local_path)
            speak("Update complete. Restarting now.")
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            os.remove(new_path)
            speak("You're already using the latest version.")
    except Exception as e:
        speak(f"Update failed: {e}")

def main():
    introduce()
    while True:
        command = input("You: ").lower()

        if command in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        elif command.startswith("open "):
            site = command.replace("open ", "").strip()
            open_site(site)
        elif command in ["shutdown", "restart"]:
            control_system(command)
        elif command in ["click", "right click", "move up", "scroll up", "scroll down"]:
            mouse_action(command)
        elif command in ["minimize", "maximize", "close"]:
            window_control(command)
        elif command == "update":
            update_self()
        else:
            answer(command)

if __name__ == "__main__":
    main()
