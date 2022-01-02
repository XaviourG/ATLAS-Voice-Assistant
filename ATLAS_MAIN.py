import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import json
#import requests

print('Loading your AI personal assistant - ATLAS')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    now = datetime.datetime.now()
    if hour >= 0 and hour < 12:
        speak("ATLAS initiating. Good Morning Sir.")
        print("ATLAS initiating. Good Morning Sir.")
    elif hour >= 12 and hour < 18:
        speak("ATLAS initiating. Good Afternoon Sir.")
        print("ATLAS initiating. Good Afternoon Sir.")
    else:
        speak("ATLAS initiating. Good Evening Sir.")
        print("ATLAS initiating. Good Evening Sir.")

    if now.minute < 16:
        speak("It is currently, " +
              str(now.minute) + " past " + str(now.hour))
    else:
        speak("It is currently, " +
              str(now.hour) + ", " + str(now.minute))
    speak("Of, " + str(now.date()))


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


wishMe()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Understood, ATLAS is halting.')
            print('Understood, ATLAS is halting.')
            break
