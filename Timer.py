import time

def main():

    ask = int(input("How many second you wante to wait?\n"))

    for i in range(ask):
        print(str(ask-i) + " Second Remain")

        time.sleep(1)

    print("Time Up!!")


    repeat = input("Would you like to run code again yes/no ?\n").lower()
    if repeat == "yes":
        main()
    else:
        print("Bye")
        exit()

main()
