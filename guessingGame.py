import random
number = random.randint(1,9)
guesses = 5
while(guesses > 0):
    guess = input('what is the number?')
    guesses = guesses - 1
    if(guess == number):
        print('You are huge brain you guess correct!')
    if(guess != number):
        print('ur wrong kid')
