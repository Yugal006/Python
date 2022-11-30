import random
import time
number = random.randint(1, 100)

player_name = input("Hello, What's your name?\n")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 100 you have 10 chances:')
print("please only use integers!")

while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
        
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('nope! '+ player_name+ ' You did not guess the number, The number was ' + str(number))
