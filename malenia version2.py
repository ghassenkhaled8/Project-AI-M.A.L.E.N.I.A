import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
from requests import get 
import pywhatkit as kit
import cv2
import sys
import time
import pyautogui
import pyjokes
import shutil
import wolframalpha
import ctypes
import winshell
from ecapture import ecapture as ec
import requests
from twilio.rest import Client
from clint.textui import progress
import json
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import tkinter
import subprocess
import feedparser
import operator
import configparser






engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<19:
        speak("Good afternoon!")
    else:
        speak("Good night!")
    speak("I am Malena sir, how can I help you")

def username():
    speak("What should i call you sir")
    uname = takecommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")



def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__=="__main__" :
    wishme()
    while True:
    # if 1:
        query = takecommand().lower() #Converting user query into lower case

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open kaggle' in query:
            webbrowser.open("kaggle.com")

        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open coursera' in query:
            webbrowser.open("coursera.org")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'what time is it?' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "D:\\bioshock\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(codePath)

        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")

        elif 'open cmd' in query:
            os.system('start cmd')

        elif 'play music' in query or "play song" in query:
            speak("Here is your music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\Ghassen Khaled\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
        
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip adress is {ip}")

        elif 'google search' in query:
            speak('what do I search')
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'youtube search' in query:
            speak('what you would like to watch?')
            cm1 = takecommand().lower()
            kit.playonyt(cm1)

        elif 'introduce yourself' in query:
            speak('I am malenia and i am an artificial intelligence created by Ghassen Khaled, i was named after the caracter from elden ring "Malenia, the blade of miquella" my purpose is to support the computer user')
        
        
        elif 'who are you?' in query:
            speak('my name is malenia, I am an artificial intelligence')

        elif 'who created you?' in query:
            speak('I was created by Ghassen Khaled')

        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'what is' in query:
            speak('searching...')
            query = query.replace('what is','')
            result = wikipedia.summary(query, sentences=2)
            speak('after a wikipidia search:')
            print(result)
            speak(result)

        elif 'who is' in query:
            speak('searching...')
            query = query.replace('who is','')
            result = wikipedia.summary(query, sentences=2)
            speak('after a wikipidia search:')
            print(result)
            speak(result)

        elif 'shutdown the system' in query:
            os.system('shutdown /s /t 5')

        elif 'restart the system' in query:
            os.system('shutdown /r /t 5')

        elif 'open camera' in query:
            cam = cv2.VideoCapture(0)
            while True:
                rec, img = cam.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cam.release()
            cv2.DestroyAllWindows()

        elif 'you can leave' in query:
            speak('ok sir, I am leaving now')
            sys.exit
        
        elif 'take a screenshot' in query:
            speak('ok sir, tell the name of the file')
            name = takecommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif 'tell us a joke' in query:
            speak(pyjokes.get_joke())

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            asname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            asname = takecommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(asname)
            print("My friends call me", asname)

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "who i am" in query:
            speak("If you can talk then definitely you are a human being.")

        elif "why you came to world" in query:
            speak("Thanks to Allah first and thanks to Ghassen. the main purpose of my existance is to serve human and getting them better experince in using intelligente systems")

        elif "who are you" in query:
            speak("I am Malenia your virtual assistant created by Ghassen Khaled")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Ghassen ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                    0,
                                                    "Location of wallpaper",
                                                    0)
            speak("Background changed successfully")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif  "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('malenia.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("malenia.txt", "r")
            print(file.read())
            speak(file.read(6))

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "malenia" in query:

            wishme()
            speak("Malenia is in your service ")
            speak(asname)

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takecommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

            else:
                speak(" City Not Found ")

        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)

                message = client.messages \
                                .create(
                                    body = takecommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )

                print(message.sid)

        elif "good morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(asname)

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = takecommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif 'offline' in query:
            speak("going Offline")
            quit()

       


        

        

        

        

        
        

            




            

        


        
