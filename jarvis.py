import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime):
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif (hour>12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("Hey Pragna, Jarvis here. Please let me know how can I help you")
    
def takecommand():
    #It takes a microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print("User said : ",query)
    except Exception as e:
        print(e)
        speak("Say that again please.....")
        return ""
    return query
    
if __name__ == '__main__':
    #speak ("Pragna is magnificent")
    wishme(datetime)
    while True:
        if 1:
            query = takecommand().lower()
        
            if 'wikipedia' in query:
                speak("Searching Wikipedia..... Please wait for a while")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                speak = ("According to Wikipedia..")
                print(results)
                #Speak results
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            #elif 'open Notepad' in query:
                #npath = "C:\\windows\\system32\\notepad.exe"
                #os.startfile(npath)
            elif 'open command prompt' in query:
                os.system('start cmd')
            elif 'open stack overflow' in query:
                webbrowser.open('stackoverflow.com')
            elif 'open calendar' in query:
                webbrowser.open('calendar.com')
            elif 'open code' in query:
                codepath = "C:\\Users\\yandu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%h:%m:%S")
                speak(f"Mam, the time is{strTime}")
            
            elif 'no thanks' in query:
                speak("Thank you Mam for using me. Have a good day!")
                break
sys.exit()
            
              
        
