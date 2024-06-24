import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui


user="sir"
engine = pyttsx3.init("sapi5") #initiate
voices = engine.getProperty('voices') #get the voices
engine.setProperty("voice", voices[0].id) #set the voices

def speak(audio):
    engine.say (audio)
    engine.runAndWait()


def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        #r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

    try:
        print("wait for few moments...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"you just said : {query}\n")
       
    except Exception as e:
        print(e)
        speak("could you tell me again sir?")
        query="none"
        commands()
    return query

def wakecommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("sleeping...")
        audio=r.listen(source)

    try:
        print("wait for few moments...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"you just said : {query}\n")
       
    except Exception as e:
        print(e)
        speak("tell me again")
        query="none"
        commands()
    return query

def wishings():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print(f"Good Morning {user}")
        speak(f"good morning {user}")
    elif hour>=12 and hour<16:
        print(f"Good afternoon {user}")
        speak(f"good afternoon {user}")
    elif hour>=16 and hour<19:
        print(f"Good evening {user}")
        speak(f"good evening {user}")
    else:
        print(f"Good night {user}")
        speak(f"good night {user}")
    
if __name__=="__main__":
    
        while True:
            query=wakecommands().lower()
            if "wake up" in query:
                print("waking up sir..")    
                speak("waking up sir")
                wishings()
                speak(f"What can i help you {user}")
                print(f"what can i help you {user}")
                while True:
                    query=commands().lower()
                    if "sleep" in query:            #sleep
                        break
                    elif "time" in query:           #time
                        strtime=datetime.datetime.now().strftime("%I:%M %p") 
                        speak(f"{user} the time is {strtime}")
                        print(strtime)
                    elif "open chrome" in query:
                        speak(f"opening chrome {user}")
                        print(f"opening chrome {user}")
                        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

                    elif "wikipedia" in query:          #search in wikipedia
                        speak("searching in wikipedia")
                        try:
                            query=query.replace("wikipedia","")
                            output=wikipedia.summary(query,sentences=1)
                            print("According to wikipedia..")
                            speak("According to wikipedia..")
                            speak(output)
                            print(output)
                        except:
                            print("not found")
                            speak("not found")
                    elif "play" in query:               #play song
                        query=query.replace('play',"")
                        speak(f"playing..{query}")
                        pywhatkit.playonyt(query)
                    elif "type" in query:                #open note pad and speak what you want to write
                        speak(f"tell me what should i type {user}")
                        while True:
                            typequery=commands()
                            if typequery=="exit typing":
                                speak("exit typing")
                                break
                            else:
                                pyautogui.write(typequery)
                    elif "minimize" in query or "minimise" in query:      #minimize the current window
                        speak(f"minimizing {user}")
                        with pyautogui.hold('win'):
                            pyautogui.press(['down', 'down',])
                    elif "maximize" in query or "maximise" in query:      #minimize the current window
                        speak(f"maximizing {user}")
                        with pyautogui.hold('win'):
                            pyautogui.press(['up', 'up',])
                    elif "close the application" in query:
                        speak(f"are you sure sir you want to close the application.. {user}")
                        while True:
                            query=commands().lower()
                            if "close it " in query:
                                speak("closing sir..")
                                with pyautogui.hold('alt'):
                                    pyautogui.press(['f4'])
                                    break
                            elif "don't close" in query:
                                speak("ok sir")
                                break
                    elif "exit program" in query or "exit the program" in query or "bye "in query:  #exit program
                        speak(f"goodbye {user} have a great day")
                        quit()
                        

