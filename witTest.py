#Author: Marcin Olko

#TODO:
    #Migrate WIT_AI_KEY to settings.json
    #Create Setup Func
    #Make better response handler
    #Make nice comments

from wit import Wit
import speech_recognition as sr

WIT_AI_KEY = "L7AZJCDKNUUZMMTLCGQVFYTHLAAHN57J"

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration = 1)
    print(r.energy_threshold)

def listen():
    # obtain audio from the microphone
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.energy_threshold = 1200
        print('Say something!')
        audio = r.listen(source)"""

    try:
        response = r.recognize_wit(audio, key = WIT_AI_KEY, show_all = True)
        print("Wit.ai thinks you said " + str(response))
        return response
    except sr.UnknownValueError:
        raise("Wit.ai could not understand audio")
    except sr.RequestError as e:
        raise("Could not request results from Wit.ai service; {0}".format(e))
