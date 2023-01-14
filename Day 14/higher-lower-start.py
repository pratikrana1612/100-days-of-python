from art import logo, vs
from replit import clear
from game_data import data
import random


def generate_users():
    """Genrate a random user from data"""
    return random.choice(data)


def print_data(message, user):
    """print user detail in formated way"""
    print(
        f"{message}: {user['name']}, {user['description']}, from {user['country']}"
    )


def user_choice(user1, user2):
    """Take user chice and check it if is A or B"""
    choice = input("Who has more followers? Type 'A' or 'B':").upper()
    if (choice == 'A'):
        return user1
    elif (choice == 'B'):
        return user2


score = 0
answer = True


def compare_choice(user1, user2, choice):
    """check the user answer and check if it is wrong or right"""
    if (user1['follower_count'] > user2['follower_count']):
        max = user1
    elif (user2['follower_count'] > user1['follower_count']):
        max = user2
    if (max == choice):
        return True
    else:
        return False


def score_increaser(answer, score): 
    """Increase the score and print score"""
    if (answer == True):
        score += 1
        print(f"You're Wrong! Current score:{score}")
    else:
        print(f"Sorry, that's wrong. Final score:{score}")
    return score


def game(answer, score):
    print(logo)
    user1 = generate_users()
    while answer:
        user2 = generate_users()
        print_data("Compare A", user1)
        print(vs)
        print_data("Against B", user2)
        choice = user_choice(user1, user2)
        answer = compare_choice(user1, user2, choice)
        user1 = user2
        clear()
        print(logo)
        score = score_increaser(answer, score)


game(answer, score)
