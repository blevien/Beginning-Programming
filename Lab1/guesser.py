from random import *

number = randint(1,100)
answer = -1
guesses = 0

while int(answer) != number:
    answer = input("Enter a number between 0 - 100: ")
    guesses = guesses + 1
    
    if int(answer) > number:
        print("Too High")
    if int(answer) < number:
        print("Too Low")

print("You Won in", guesses, "guesses!")
