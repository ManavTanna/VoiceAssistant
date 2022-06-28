from importlib.resources import path
import pyttsx3
import speech_recognition as sr
import datetime
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("Repeat again please...")
        return "none"
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 4 and hour < 12:
        speak("Good Morning Master")

    elif  hour >= 12 and hour < 16:
        speak("Good Afternoon Master")

    elif  hour >= 16 and hour < 22:
        speak("Good Evening Master")

    else:
        speak("Good Night Master")

    speak("Hello Master, it's good to have you here today. How can I help you?")




if __name__ == "__main__":
    wishme()
    #while True:
    if 1:

        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "Open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()
