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

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "D:\\bioshock\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to cg4' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "cg4wock@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend cg4. I am not able to send this email") 

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(codePath)

        elif 'open cmd' in query:
            os.system('start cmd')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Ghassen Khaled\\Music'
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        
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
        
        elif 'open webcam' in query:
            speak('ok sir, just a moment')
        
        elif 'who are you?' in query:
            speak('my name is malenia, I am an artificial intelligence')

        elif 'who created you?' in query:
            speak('I was created by Ghassen Khaled')

        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        
        

            




            

        


        
