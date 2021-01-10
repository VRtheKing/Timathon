import pyttsx3
engine = pyttsx3.init() 
engine.setProperty('rate', 178) 

def speak(command):
    engine.say(command)
    engine.runAndWait()


