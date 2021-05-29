# simple guessing game
# uses if,loop,list and random generator
import random
import numpy as np

TRUE = 1
FALSE = 0
tries_per_game =[]
tries = 1
another_game ='Y'
print("guess a number from 1 to 99")

number = random.randint(1,99)

while(another_game.upper() == 'Y'):
    correct_guess = FALSE

    while(correct_guess == FALSE):
        try:
            guess = int(input("enter a guess : "))
        except:
            print("please enter a number")
            continue


        if guess == number:
            print('you are right!')
            print(f"number ={number} ; tries ={tries}")

            correct_guess = TRUE
            tries_per_game.append(tries)
        elif guess>number:
            print('lower')
            tries+= 1
        else:
            print('higher')
            tries += 1
    


    another_game = input("try another number?[y/n] :")
    if another_game.upper()== 'Y':
        number = random.randint(1,99)
        tries =0

print("analyzing results..")

print(f"result = {tries_per_game}")
print(f"mean score = {np.mean(tries_per_game)}")
print(f"median = {np.median(tries_per_game)}")
print(f"average = {np.average(tries_per_game)}")
print(f"standard deviation = {np.std(tries_per_game)}")


print("ending game")