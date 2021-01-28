from youtube3 import YoutubeClient
import wikipedia
from datetime import datetime
from pywhatkit import playonyt, search
import pyjokes



now = datetime.now()



#speak_commands
class speak_commands():
    def speak(self, command):
        command =command
        x = command
        if 'YouTube' in x:
            x = command.replace('YouTube','')
            play = 'playing'+ x
            print(play)
            self.playonyt(x)
            return play

        elif 'search' in x:
            x = command.replace('search','')
            searching = 'searching' + x
            print(searching)
            search(x)
            return searching
        elif 'Wikipedia' in x:
            x = command.replace('Wikipedia', '')
            try:
                ans = wikipedia.summary(x, sentences = 1)
                print(ans)
                return ans
            except:
                return 'retry'

        elif 'joke' in x:
            return pyjokes.get_joke()
        else:
            return 'retry'



    def playonyt(self,vid):
        playonyt(vid)
