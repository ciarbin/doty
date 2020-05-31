#Author: Marcin Olko

#TODO:
    #Change TextToSpeechClient for somenthing faster, and not requiring internet connection (pyttsx3)

from gtts import gTTS
from playsound import playsound
import os
import sys

def say(text):
    """
    Function that reads given string.
    """
    tts = gTTS(text=text, lang='pl', slow = False)
    filename = './resources/ttstmp.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove('./resources/ttstmp.mp3')
