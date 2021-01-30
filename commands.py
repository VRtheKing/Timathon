from youtube3 import YoutubeClient
import wikipedia
from datetime import datetime
from pywhatkit import playonyt, search
import pyjokes
import webbrowser
import time
import backend_api
import random
from PyDictionary import PyDictionary

now = datetime.now()



#speak_commands
class speak_commands():
    def speak(self, command):
        command = command
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

        elif 'locate' in x or 'location' in x:
            x = command.replace('locate', '')
            return webbrowser.open(f'https://www.google.co.in/maps/place/{x}')

        elif '8 ball'in x:
            l = self.ball8()
            print(l)
            return l

        elif 'synonyms of' in x or 'synonym of' in x:
            x = command.replace('synonyms of ','')
            x = command.replace('synonym of ','')
            l = self.synonyms(x)
            return l

        elif 'antonyms of' in x or 'antonym of' in x:
            x = command.replace('antonyms of ','')
            x = command.replace('antonym of ','')
            l = self.antonyms(x)
            return l

        elif 'Amazon find' in x:
            x = command.replace('Amazon find', '')
            return backend_api.searchamazon(x)

        elif 'stack' in x:
            x = command.replace('stack','')
            return backend_api.searchstack(x)
        elif 'Flipkart find' in x:
            x = command.replace('Flipkart find', '')
            return backend_api.searchflip(x)
        else:
            return 'retry'

    def playonyt(self,vid):
        playonyt(vid)

    def ball8(self):
        responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes',
                 'Very doubtful.',
                 'Without a doubt',
                 'Yes',
                 'No',
                 'you may rely on it',
                 'definitely']
        return random.choice(responses)

    def synonyms(self, x):
        x = x.replace(' ','')
        print(x)
        dictionary=PyDictionary()
        try:
            print( dictionary.synonym(x))
            return  dictionary.synonym(x)
        except:
            return 'retry'

    def antonyms(self, x):
        x = x.replace('','')
        dictionary=PyDictionary()
        try:
            print( dictionary.antonym(x))
            return  dictionary.antonym(x)
        except:
            return 'retry'
