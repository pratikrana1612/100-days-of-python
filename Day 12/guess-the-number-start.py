#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
EASY_LEVEL = 10
HARD_LEVEL = 5
number = random.randint(1, 100)
print(number)


def check_answer(guess,number):
    if (guess == number):
        print(f"You have guessed it it is {number}")
        return True
    elif (guess > number):
        print("Too high")
    elif (guess < number):
        print("Too low")
    else:
        print("Enter valid number")
    print("Guess again")
    return False

def level():
    choice = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    if (choice == 'hard'):
        return HARD_LEVEL
    else:
        return EASY_LEVEL

chances = level()
guessed = False

while chances > 0 and not guessed:
    print(f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    guessed=check_answer(guess,number)
    chances-=1

if (not guessed):
    print("Attempts are finished You lose")