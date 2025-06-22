import speech_recognition as sr
import pyttsx3
import subprocess

# Text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command
    except:
        speak("Sorry, I didn’t catch that.")
        return ""

def ask_local_llm(prompt):
    # Pass the prompt as an argument (not via stdin)
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

# Main loop
while True:
    query = listen()
    if query.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye.")
        break
    reply = ask_local_llm(query)
    speak(reply)
