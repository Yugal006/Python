import pywhatkit as pwt

def main():
    ask = input("Search Google or Type URL\n")

    pwt.search(ask)

    repeat = input("Would you like to run code again yes/no ?\n").lower()
    if repeat == "yes":
        main()
    else:
        print("Bye")
        exit()
main()
