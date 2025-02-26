import os
import platform

def speak(text):
    """Convert text to speech using the appropriate command for the OS."""
    system_name = platform.system()
    if system_name == "Darwin":  # macOS
        os.system(f"say {text}")
    elif system_name == "Linux":
        os.system(f"espeak '{text}'")
    elif system_name == "Windows":
        # Use PowerShell to load the System.Speech assembly and speak the text
        os.system(f"PowerShell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')\"")
    else:
        print("Unsupported operating system")

if __name__ == '__main__':
    print("Welcome to the RoboSpeaker")
    while True:
        x = input("What do you want to say? ")
        if x.lower() == "quit":
            print("Goodbye!")
            break
        speak(x)