import pyttsx3
engine = pyttsx3.init() 
engine.setProperty('rate', 178) 

def speak(command):
    while True:
        engine.say(command)
        engine.runAndWait()
        return False
    engine.stop()


