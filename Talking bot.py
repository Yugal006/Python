import pyttsx3
def main():
    engine = pyttsx3.init()
    V = int(input('choose voices "0" for girl "1" for boy:\n'))
    voices = engine.getProperty('voices')
    volume = engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[V].id) 
    ask = input("type to hear voice\n")
    engine.say(ask)
    engine.runAndWait()

    repeat = input("Would you like to run code again yes/no ?\n").lower()
    if repeat == "yes":
        main()
    else:
        print("Bye")
        exit()

main()
