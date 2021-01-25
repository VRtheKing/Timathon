import speech_recognition as sr
import speak
from youtube3 import YoutubeClient
import wikipedia
from datetime import datetime
import pyautogui

pyautogui.moveTo(100, 200)
pyautogui.moveTo(200, 300)

from pywhatkit import playonyt, search

now = datetime.now()


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



        if 'youtube' in x:
            x = self.command.replace('youtube','')
            play = 'playing'+ x
            print(play)
            speak.speak(play)
            self.playonyt(x)
        elif 'time' in x:
            current_time = now.strftime("%H:%M")
            speak.speak("Current Time is" + current_time)

        elif 'search' in x:
            x = self.command.replace('search','')
            searching = 'searching' + x
            print(searching)
            speak.speak(searching)
            search(x)
        elif 'Wikipedia' in x:
            x = self.command.replace('Wikipedia', '')
            try:
                ans = wikipedia.summary(x, sentences = 3)
                print(ans)
                speak.speak(ans)
            except:
                speak.speak('retry')


    def playonyt(self,vid):
        playonyt(vid)
