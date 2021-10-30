import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit

global text



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate','100')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<=12:
        speak("Good Morning")
    elif 12<hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    time.sleep(0.1)
    speak("I am GOAT , greatest of all times")
    speak("How can I help you?")

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        #r.energy_threshold = 200
        #r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")

        text=r.recognize_google(audio,language='en-in')
        #print("User said this ",search)
        return text.lower()
    except:
        print("Say that again please...")
    
    
    

if __name__ == '__main__':
    speak("Hello boss")
    time.sleep(0.1)
    wishme()
    while(True):
        query=command()
        if 'wikipedia' in query :
            speak("Searching wikipedia")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url='youtube.com/'
            webbrowser.get(chrome_path).open(url)
        elif 'on youtube' in query:
            video=command().lower()

            pywhatkit.playonyt(video)
        elif 'open google' in query:
            url='google.com/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)  
        elif 'play music' in query:
            music_dir='C:\\Users\\LENOVO\\Music'
            songs=os.listdir(music_dir)
            num=len(songs)
            rand=random.randrange(0,num+1)
            #print(rand)
            os.startfile(os.path.join(music_dir,songs[rand]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , time is {strtime}")
        elif 'open vs' in query:
            path='C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code'
            os.startfile(path)
        elif 'send email' in query:
            email()
        elif 'whatsapp' in query:
            numbers={
            '<name>':'<number with country code>'
    
            }
            speak('To whom you wanna send message')
            number=command().lower()
            digit=numbers[number]
            speak('Say the text')
            text=command()
            pywhatkit.sendwhatmsg(digit,text,datetime.datetime.now().hour,(datetime.datetime.now().minute+1))
        elif 'quit' in query:
            speak('Thank you for your time Sir')
            exit()
        else:
            speak('Can you please repeat what you said?')
            command()
            
        
            




