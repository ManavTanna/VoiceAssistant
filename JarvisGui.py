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
from jarvisUI import Ui_JarvisUI
from PyQt5 import QtCore , QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


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
    server.sendmail('manavjtanna@gmail.com', to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
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

    def TaskExecution(self):

        if __name__ == "__main__":

            wish()
            while True:

                self.query = self.takecommand().lower()

                # logic building for tasks

                if "open notepad" in self.query:
                    npath = "C:\\Windows\\notepad.exe"
                    os.startfile(npath)



                elif "open command prompt" in self.query:
                    os.system("start cmd")


                elif "open camera" in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break;
                    cap.release()
                    cv2.destroyAllWindows()

                elif "play music" in self.query:
                    music_dir = "P:\\music"
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(music_dir, rd))


                elif "ip address" in self.query:
                    ip = get('http://api.ipify.org').text
                    speak(f"your IP address is {ip}")

                elif 'switch the window' in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "temperature in" in self.query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")


                elif "wikipedia" in self.query:
                    speak("search in wikipedia..")
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("according to wikipedia")
                    speak(results)
                    print(results)

                # to set alarm
                elif "set alarm" in self.query:
                    nn = int(datetime.datetime.now().hour)
                    if nn == 22:
                        music_dir = 'P:\\music'
                        songs = os.listdir(music_dir)
                        os.startfile(os.path.join(music_dir, songs[0]))


                elif "open youtube" in self.query:
                    webbrowser.open("www.youtube.com")

                # elif "send message" in query:
                #   kit1.sendwhatmsg("+919960368206","voice assistant message",10,10)

                elif "open google" in self.query:
                    speak("sir, what should i search on google")
                    cm = self.takecommand().lower()
                    webbrowser.open(f'{cm}')

                elif "email to manav" in self.query:
                    try:
                        speak("what should i say?")
                        content = self.takecommand().lower()
                        to = "manavjtanna@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent to manav")

                    except Exception as e:
                        print(e)
                        speak("sorry sir, i am not able to send this message to pratham")


                elif "no thanks" in self.query:
                    speak("thanks for using me sir, have a good day.")
                    sys.exit()

                speak("sir, do you have any other work")

startExecution = MainThread()

class Main1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movies_3 = QtGui.QMovie("Earth.gif")
        self.ui.label_3.setMovie(self.ui.movies_3)
        self.ui.movies_3.start()

        self.ui.movies_5 = QtGui.QMovie("Iron_Template_1.gif")
        self.ui.label_5.setMovie(self.ui.movies_5)
        self.ui.movies_5.start()

        self.ui.movies_7 = QtGui.QMovie("B.G_Template_1.gif")
        self.ui.label_7.setMovie(self.ui.movies_7)
        self.ui.movies_7.start()

        self.ui.movies_4 = QtGui.QMovie("jZqDPB.gif")
        self.ui.label_4.setMovie(self.ui.movies_4)
        self.ui.movies_4.start()

        self.ui.movies_6 = QtGui.QMovie("f88acab7ffd127b4465659500aa0538f.gif")
        self.ui.label_6.setMovie(self.ui.movies_6)
        self.ui.movies_6.start()

        self.ui.movies_10 = QtGui.QMovie("loading_1.gif")
        self.ui.label_10.setMovie(self.ui.movies_10)
        self.ui.movies_10.start()

        self.ui.movies_11 = QtGui.QMovie("Hero_Template.gif")
        self.ui.label_11.setMovie(self.ui.movies_11)
        self.ui.movies_11.start()

        self.ui.movies_8 = QtGui.QMovie("__02-____.gif")
        self.ui.label_8.setMovie(self.ui.movies_8)
        self.ui.movies_8.start()

        self.ui.movies_9 = QtGui.QMovie("1.gif")
        self.ui.label_9.setMovie(self.ui.movies_9)
        self.ui.movies_9.start()

        #timer = QTimer(self)
        #timer.timeout.connect(self.showTime)
        #timer.start(5000)
        startExecution.start()

   # def showTime(self):
        #current_time = QTime.currentTime()
        #now = QDate.currentDate()
        #lable_time = current_time.toString('hh:mm:ss')

app = QApplication(sys.argv)
JarvisGui = Main1()
JarvisGui.show()
exit(app.exec_())
