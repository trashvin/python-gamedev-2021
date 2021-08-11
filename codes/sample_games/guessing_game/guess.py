# simple guessing game
# uses if,loop,list and random general

import random

number = random.randint(0,100)

correct_guess = False

while(correct_guess == False):
    try:
        guess = int(input("Enter your guess number : "))

        if guess == number:
            print("you are correct")
            print(f"the generated number is {number}")

            correct_guess = True
        elif guess < number:
            print("the number is higher")
        else:
            print("the number is lower")

    except:
        print("please enter a valid number")


    






