import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('L6KTH5-HWVH53A2QV')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am Shelli Volume 1!')
speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while  True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query or 'youtube kholo' in query:
            speak('okay')

            webbrowser.open('www.youtube.com')

        elif 'lights on' in query:
            speak('lights on')

        elif 'lights off' in query:
            speak('lights off')

        elif 'open google' in query or 'google kholo' in query:
            speak('okay')
            webbrowser.open('www.google.com')

        elif 'open word' in query or 'word kholo' in query:
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office15\WINWORD.exe')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'chalo niklo ab' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query or 'see yeah' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('The internet says')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('According to WIKIPEDIA ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Anything Else! Sir!')

