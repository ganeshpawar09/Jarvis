import pyttsx3 
import speech_recognition
import datetime
import wikipedia
import webbrowser
from playsound import playsound
import pyautogui
from PIL import Image
import requests
from bs4 import BeautifulSoup
import os
import time
import wolframalpha
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer , QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow
from jarvisui import Ui_MainWindow

assistant = pyttsx3.init("sapi5")
assistant.setProperty("rate",175)
assistant.setProperty("volume",1.0)
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[0].id)

def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def welcome():
    location = "Pune"           
    search = f'Weather in {location}'
    url = f'https://www.google.com/search?&q={search}'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    a=time.strftime("%I:%M %p")
    playsound("C:\\Users\\gapaw\\Desktop\\CODING\\JARVIS\\WhatsApp-Audio-2022-04-26-at-5.23.01-PM.wav")
    playsound("C:\\Users\\gapaw\\Desktop\\CODING\\JARVIS\\WhatsApp-Audio-2022-04-26-at-5.23.05-PM.wav")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak(f"Good Morning sir. It's {a}. The temperature of Pune is {temp}")
        print(f"Good Morning sir. It's {a}. The temperature of Pune is {temp}")
    elif hour>12 and hour<18:
        speak(f"Good afternoon sir. It's {a}. The temperature of Pune is {temp}") 
        print(f"Good afternoon sir. It's {a}. The temperature of Pune is {temp}") 
    else:
        speak(f"Good evening sir, it's {a}. The temperature of Pune is {temp}")
        print(f"Good evening sir, it's {a}. The temperature of Pune is {temp}")
    
    speak("Tell me how may I help you")
def super_intelligent_ai(que):
        try:
            my_id="2VX6AR-J87WL3LGE5"
            client = wolframalpha.Client(my_id)
            res = client.query(que)
            ans = next(res.results).text
            return ans
        except:
            return "None"         
class MainThread(QThread):
    def __init__(self) -> None:
        super(MainThread,self).__init__()
    def run(self) -> None:
        self.Main()

    def querytaker(self):
        #It takes microphone input from the user and returns string output

        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone(device_index=0) as source:
            print("Listening...")
            speak("Listening...")

            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")   
            speak("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")  
            return "None"
        return query
    
    def Main(self):
        welcome()
        while True:
            self.query = self.querytaker().lower()

            if "information about" in self.query or "tell me" in self.query:    
                speak('Searching Wikipedia...')
                try:
                    self.query = self.query.replace("information about","").replace("tell me","")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except:
                    print("An Unexpexted Error!")
                    speak("An Unexpexted Error!")
                
            elif 'none' in self.query:
                print(f"You what to search ,{self.query}?")
                speak(f"You what to search ,{self.query}?")
                a=self.querytaker().lower()
                if a=="yes":
                    speak("ok")
                    webbrowser.open(f"{self.query}.com")
            
            elif "temperature" in self.query :
                print("Temperature of which city?")
                speak("Temperature of which city?")
                location = self.querytaker().lower()
                
                search = f'Weather in {location}'
                url = f'https://www.google.com/search?&q={search}'
                html = requests.get(url).content
                
                soup = BeautifulSoup(html, 'html.parser')
                temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                speak(f'Current Temperature of {location} is {temp}')
                print(f'Current Temperature of {location} is {temp}')


            elif 'open youtube' in self.query or 'youtube' in self.query :
                speak("Launching youtube for you sir!")
                webbrowser.open("youtube.com")
 
            
            elif 'open dashboard' in self.query or 'dashboard' in self.query :
                speak("Launching dashboard for you sir!")
                webbrowser.open('https://docs.google.com/document/d/14qNvVJIWGXZCRII5_58ZrPRW8UpbAM3MEQbKq4obUL0/edit')
               

            elif 'open google' in self.query or 'google' in self.query :
                speak("Launching google for you sir!")
                webbrowser.open("google.com")
                
                
            elif 'open vs code' in self.query or 'code' in self.query :
                speak("Launching visual studio code for you sir!")
                codePath = "C:\\Users\\gapaw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                

            elif 'open whatsapp' in self.query or "open what's app" in self.query or 'whats app' in self.query or "what's aap" in self.query  :
                speak("Launching what's app for you sir!")
                codePath = "C:\\Users\\gapaw\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(codePath)
              
                
                
            elif 'open telegram' in self.query or  'telegram' in self.query :
                speak("Launching telegram for you sir!")
                codePath = "C:\\Users\\gapaw\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                os.startfile(codePath)
                

            elif 'open chrome' in self.query or 'chrome' in self.query :
                speak("Launching chrome for you sir!")
                codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)
                
              

            elif 'open excel' in self.query or 'excel' in self.query  :
                speak("Launching excel for you sir!")
                codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(codePath)
                
            
            
            elif 'open powerpoint' in self.query or 'powerpoint' in self.query  :
                speak("Launching powerpoint for you sir!")
                codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(codePath)
                
            

            elif 'open word' in self.query :
                speak("Launching word for you sir!")
                codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(codePath)
                
            

            elif "set alarm" in self.query or "alarm" in self.query:
                speak("Enter the hours !")
                hrs=int(input("Enter the hours (00) :"))
                speak("Enter the minutes !")
                min=int(input("Enter the minutes (00) :"))
                speak("Enter the PM or AM")
                pmam=input("Enter the pm or am :")
                if pmam=="pm":
                    hrs+=12
                

                while True:
                    if hrs==datetime.datetime.now().hour and min==datetime.datetime.now().minute:
                        playsound("C:\\Users\\gapaw\\Downloads\\ring.mp3.wav")
                    elif min+1==datetime.datetime.now().minute:
                        break
                
                
            
            elif "take screenshot" in self.query or "take a screenshot" in self.query or "capture the screen" in self.query:
                speak("By what name do you want to save the screenshot?")
                name = self.querytaker().lower()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")  
                
            

            elif "show me the screenshot" in self.query or "show screenshot" in self.query:
                speak("Name of the image is?")
                nam =self.querytaker().lower
                try:
                    img = Image.open(f"C:\\Users\\gapaw\\Desktop\\JARVIS\\{nam}.png")
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)
                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")


            elif "volume up" in self.query or "increase volume" in self.query:
                pyautogui.press("volumeup")
                speak('volume increased')
                


            elif "volume down" in self.query or "decrease volume" in self.query:
                pyautogui.press("volumedown")
                speak('volume decreased')
               

                
            elif 'your name' in self.query or "whats your name" in self.query:
                speak('My name is JARVIS')


            elif 'who made you' in self.query:
                speak('I was created by Ganesh in 2022')


            elif 'jarvis stands for' in self.query or "full form of jarvis" in self.query:
                speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')


            elif "close the window" in self.query or "close window" in self.query:
                speak("Okay sir, closing the window")
                pyautogui.keyDown("alt")
                pyautogui.press("f4")
                time.sleep(1)
                pyautogui.keyUp("alt")
                

            elif "wait" in self.query:
                speak("Waiting")
                time.sleep(30)
                print("tell me how may I help you")
                speak("tell me how may I help you")


            elif "goodbye" in self.query or "bye" in self.query or "stop" in self.query or "offline" in self.query or "exit" in self.query:
                print("Alright sir, going offline. It was nice working with you, have a nice day!")
                speak("Alright sir, going offline. It was nice working with you, have a nice day!")
                sys.exit()

            else:
                que=self.query
                a= super_intelligent_ai(que)
                if "noun" in a or "Noun" in a:
                    print(f"You what to search ,{self.query}?")
                    speak(f"You what to search ,{self.query}?")
                    a=self.querytaker().lower()
                    if "yes" in a:
                        speak("ok")
                        webbrowser.open(f"{self.query}.com")
                elif a!="None":
                    print(a)
                    speak(a)
                else:
                    print(f"You what to search ,{self.query}?")
                    speak(f"You what to search ,{self.query}?")
                    a=self.querytaker().lower()
                    if "yes" in a:
                        speak("ok")
                        webbrowser.open(f"{self.query}.com")
                   

                        
startExecution=MainThread()
class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie=QtGui.QMovie("2264c-jarvis-1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app= QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())