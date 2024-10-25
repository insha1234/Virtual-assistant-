# Virtual Assistant

This is a simple voice-activated virtual assistant created using Python. The assistant can perform various tasks such as searching Wikipedia, opening web pages, telling the current time, and more, based on voice commands.

## Features

- **Speech Recognition**: Listens to the user's voice and converts it to text.
- **Text-to-Speech**: Converts text responses into spoken words.
- **Wikipedia Integration**: Fetches brief summaries from Wikipedia.
- **Web Browsing**: Opens popular websites like Google and YouTube.
- **Time Telling**: Provides the current time.
- **Command Execution**: Can open applications, such as VS Code.
- **Exit Command**: Ends the assistant's session.

## Prerequisites

Before running the virtual assistant, make sure you have the following Python libraries installed:

- `SpeechRecognition`: For converting speech to text.
- `pyttsx3`: For text-to-speech conversion.
- `wikipedia`: For fetching information from Wikipedia.
- `webbrowser`: For opening web pages.
- `datetime`: For retrieving the current date and time.
- `os`: For accessing system files.
- `pyaudio`: For capturing audio input (required by `SpeechRecognition`).

You can install the required libraries with the following commands:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install wikipedia
pip install pyaudio
