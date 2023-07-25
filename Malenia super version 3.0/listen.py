import speech_recognition as sr

def listen():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except:
        return "" #None string will be returned
    
    
    query = str(query)
    return query.lower()
