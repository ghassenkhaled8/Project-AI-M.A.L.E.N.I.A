import pyttsx3



def say(Text):
    engine = pyttsx3.init('sapi5')
    voices= engine.getProperty('voices') #getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    print('   ')
    print(f"Malenia : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print('   ')