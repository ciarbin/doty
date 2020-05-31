#Author: Marcin Olko

#TODO:
    #Make better command handeling
    #Make settings.json for storing User preferences

import tts
import greetings
import witTest
import jokes

def main():

    koniec = False

    while not koniec:
        try:
            command = witTest.listen()['entities']['intent'][0]['value']
        except:
            command = "error"
        if command == 'greetings':
            greetings.greetings()

        elif command == "joke":
            jokes.say()

        elif command == "close":
            koniec = True

        elif command == "error":
            tts.say("Przepraszam, nie zrozumiałem. Mógłbyś powtórzyć?")

    tts.say("Dobrej nocy")

if __name__ == '__main__':
    main()
