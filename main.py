import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os

# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set properties for text-to-speech
tts_engine.setProperty('rate', 150)  # Speed of speech
tts_engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Function to make the assistant speak
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to recognize the user's voice input
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Pause before the assistant starts recognizing
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Please say it again.")
        return None
    return query

# Function to execute tasks based on commands
def execute_command(query):
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("The term you searched for has multiple meanings. Please be more specific.")
        except Exception as e:
            speak("Sorry, I could not find information on that topic.")

    elif 'open youtube' in query.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'the time' in query.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif 'open code' in query.lower():
        code_path = "C:\\Path\\To\\Your\\VSCode\\Code.exe"  # Update with the path to your code editor
        os.startfile(code_path)

    elif 'exit' in query.lower() or 'stop' in query.lower():
        speak("Goodbye! Have a great day!")
        exit()

    else:
        speak("I'm sorry, I don't know how to do that.")

# Main function to run the virtual assistant
def run_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        command = take_command()
        if command:
            execute_command(command)

if __name__ == "__main__":
    run_assistant()
