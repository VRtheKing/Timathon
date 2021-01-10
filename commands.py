import speech_recognition as sr
import speak
from youtube3 import YoutubeClient 
from pywhatkit import playonyt
from datetime import datetime

now = datetime.now()

import pyautogui

pyautogui.moveTo(100, 200)
pyautogui.moveTo(200, 300)
listener = sr.Recognizer()

#take_commands area
def take_commands():
        try:
            with sr.Microphone() as source:
                print('listening')
                audio = listener.listen(source)
                text  = listener.recognize_google(audio)
                print(text)
                return text
        except Exception as e:
            print(e)
            speak.speak('retry')
       

#speak_commands
class speak_commands():
    def __init__(self,command):
        self.command = command
    
        if 'new' in self.command:
            x = self.command.replace('new','')
            print(x)

            if 'hello' in x:
                speak.speak('hello, What can i do for you')
            
            elif 'play' in x:
                x = self.command.replace('new play','')
                play = 'playing'+ x
                print(play)
                speak.speak(play)
                self.playonyt(x)
            elif 'time' in x:
                current_time = now.strftime("%H:%M")
                speak.speak("Current Time is" + current_time)
        
    def playonyt(self,vid):
        playonyt(vid)


command = take_commands()     
speak_command = speak_commands(command)
