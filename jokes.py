#Author: Marcin Olko

#TODO:
    #More jokes!!!!!

import tts
import random
import time

JOKES = [
["Dlaczego Napoleon jedzie windą na dół?", "Bonaparter"],
["Jak się nazywa skrzyżowanie psa z rybą", "Dalmatuńczyk"],
["Informatyk do informatyka: - Pożycz mi 500 zł - Masz tu 512 dla równego rachunku"],
["Jaka jest najszybsza rasa kota?", "Kot spadający z dachu"],
["Po wodzie pływa i kaczka się nazywa", "Kaczka"],
]

def say():
    """
    Function that tells rondom joke from the JOKES table.
    """
    joke = random.choice(JOKES)
    if len(joke) == 1:
        tts.say(joke[0])
    elif len(joke) == 2:
        tts.say(joke[0])
        #time.sleep(0)
        tts.say(joke[1])
