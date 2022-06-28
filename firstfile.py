import os
import time

import pyttsx3
import speech_recognition as sr
import datetime
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import sys
import smtplib
import pyautogui
import requests
from bs4 import BeautifulSoup

# import pywhatkit as kit1


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print('"recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good morning")

    elif hour > 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("Good evening")
    speak("i am jarvis sir, please tell me how can i help you")


# to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('psuroshi9@gmail.com', '8378083668')
    server.sendmail('psuroshi9@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)



        elif "open command prompt" in query:
            os.system("start cmd")


        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "P:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "temperature in" in query:
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")


        elif "wikipedia" in query:
            speak("search in wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        # to set alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'P:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        # elif "send message" in query:
        #   kit1.sendwhatmsg("+919960368206","voice assistant message",10,10)

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f'{cm}')

        elif "email to pratham" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "psuroshi9@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to pratham")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this message to pratham")


        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir, do you have any other work")

    # takecommand()
    # speak("hello sir")
