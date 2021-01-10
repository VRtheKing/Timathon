import speech_recognition as sr


Listener = sr.Recognizer()

def take_commands():
        try:
            with sr.Microphone() as source:
                print('listening')
                audio = Listener.listen(source)
                text  = Listener.recognize_google(audio)
                print(text)
        except:
            print('retry')

        


take_commands()            