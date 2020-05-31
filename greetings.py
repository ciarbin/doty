#Author: Marcin Olko

#TODO:
    #Improve code readability
    #Make it more flexible

import tts
import time
import locale
import calendarcli
import witTest
import datetimemanager

def setup():
    locale.setlocale(locale.LC_TIME, "pl")

def greetings():
    """
    Function welcoming you to the new day and reading you the interesting infos for today and maybe more. ;)
    """
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    date = time.strftime("%d %B", t)
    tts.say("Witaj Marcin! Dzisiaj jest " + date + ", godzina " + current_time)

    timeMax = datetimemanager.from_time_to_RFC3339(time.localtime(time.time() + 60*60*24))
    events = calendarcli.list_events(timeMax = timeMax)
    if len(events) > 0:
        tts.say("Na najbliższe 24 godziny masz zaplanowane '" + str(len(events)) + "' wydarzeń.")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))[:10]
            start = time.strptime(start, "%Y-%m-%d")
            start = time.strftime("%d %B", start)
            tts.say(event["summary"] + ". Zaczynające się " + start)
    else:
        tts.say("Na najbliższe 24 godziny nie masz nic zaplanowane")

    tts.say("Czy chcesz żebym przeczytał twoje plany na najbliższy tydzień?")
    response = witTest.listen()
    if response == "yes":

        timeMin = datetimemanager.from_time_to_RFC3339(time.localtime(time.time() + 60*60*24))
        timeMax = datetimemanager.from_time_to_RFC3339(time.localtime(time.time() + 60*60*24*7))
        events = calendarcli.list_events(timeMin = timeMin, timeMax = timeMax)
        if len(events) > 0:
            tts.say("W ciągu najbliższego tygodnia masz zaplanowane '" + str(len(events)) + "' wydarzeń.")
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))[:10]
                start = time.strptime(start, "%Y-%m-%d")
                start = time.strftime("%d %B", start)
                tts.say(event["summary"] + ". Zaczynające się " + start)
        else:
            tts.say("Na najbliższy tydzień nie masz nic zaplanowane")

    elif response == "no":
        tts.say("Dobrze")
    else:
        tts.say("Rozumiem to jako nie. Jeśli jednak zmienisz zdanie, wiesz gdzie się zgłosić")

    tts.say("To wszystko na teraz, miłego dnia!")

if __name__ == 'greetings':
    setup()
