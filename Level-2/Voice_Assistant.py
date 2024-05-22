This Python code is for a virtual assistant that can be controlled by voice commands. Here's a breakdown of what the code does:

1.Imports: It starts by importing libraries for speech recognition (speech_recognition), text-to-speech (pyttsx3), web browsing (webbrowser), date and time manipulation (datetime), file operations (os), and making web requests (requests).
2.Initialization: It creates a recognizer object to listen for audio and convert it to text, and a text-to-speech engine to speak back responses.
3.Functions:
*speak(text): Converts the given text to speech and speaks it out loud.
*listen(): Listens for voice input, recognizes the speech using Google Speech Recognition service, and returns the recognized text in lowercase. If it can't understand the speech, it returns "None".
*open_website(url): Opens the specified website URL in a web browser and speaks a confirmation message.
*get_weather(city): Fetches weather information for a city using an OpenWeatherMap API key. It speaks the current temperature in Celsius and weather description for the city. If the city is not found, it speaks an error message.
*get_time(): Gets the current time and speaks it out loud.
*play_music(): Plays the first music file found in a specified directory using the system's default music player. It speaks a message if no music files are found.
*perform_task(query): Takes a recognized voice command (query) and performs different actions based on the keywords in the command. It can open Youtube or Google in the web browser, get the weather for a city, play music, or exit the program.
4.Main loop: The code starts by speaking a greeting message. Then, it enters a loop that continuously listens for user commands. If a valid command is recognized, it calls the perform_task function to handle the request. The loop continues until the user says "exit".

In summary, this code provides a basic virtual assistant that can respond to voice commands for web browsing, weather information, playing music, and more.


import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import requests

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio input and recognize speech"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"
    return query.lower()

def open_website(url):
    """Open a website"""
    webbrowser.open(url)
    speak(f"Opening {url}")

def get_weather(city):
    """Fetch and speak the weather information"""
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature - 273.15:.2f} degrees Celsius with {weather_desc}.")
    else:
        speak("City not found.")

def get_time():
    """Fetch and speak the current time"""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def play_music():
    """Play music from a specified directory"""
    music_dir = 'YOUR_MUSIC_DIRECTORY_PATH'
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music.")
    else:
        speak("No music files found in the directory.")

def perform_task(query):
    """Perform tasks based on the recognized query"""
    if 'open youtube' in query:
        open_website("https://www.youtube.com")
    elif 'open google' in query:
        open_website("https://www.google.com")
    elif 'time' in query:
        get_time()
    elif 'weather' in query:
        speak("Which city?")
        city = listen()
        if city != "None":
            get_weather(city)
    elif 'play music' in query:
        play_music()
    elif 'exit' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command. Please try again.")

if _name_ == "_main_":
    speak("How can I assist you today?")
    while True:
        query = listen()
        if query and query != "None":
            perform_task(query)
