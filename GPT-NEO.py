#from traceback import print_list
#pip -m install pyttsx3 googletrans==4.0.0-rc1
from googletrans import Translator
import pyttsx3 as ttv
#from googletrans import Translator
translator = Translator()
traductor= translator.translate('New York (CNN)After announcing he wants out of his deal to buy Twitter, Elon Musk, spent the weekend in Idaho at the Sun Valley Conference 1,000,000.\nHe spoke on stage, essentially off the record, but a source in the room told CNN is chief media correspondent Brian Stelter that Musk tripled down on his decision to try to back out of the deal and claiming it is all about the bots.',dest='es')
#print_list(traductor)
voz=traductor.text
print(voz)

#iniciando pyttsx3
engine = ttv.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
voices = engine.getProperty('voices') #
print (rate)                        #printing current voice rate
print(voices)
engine.setProperty('rate', 130)     # setting up new voice rate
engine.setProperty('voice', voices[0].id) 
#engine.say("I will speak this text")
engine.say(voz)
engine.runAndWait()
engine.stop()
