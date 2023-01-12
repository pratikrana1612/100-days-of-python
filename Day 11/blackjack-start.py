############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project. i choosed

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
import random
from replit import clear

user_cards = []
computer_cards = []

def card_choicer():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
  
def card_picker():
    for _ in range(2):
      user_cards.append(card_choicer())
      computer_cards.append(card_choicer())
    # if (turn == 'user'):
    #     if (len(user_cards) == 0):
    #         card1 = card_choicer
    #         card2 = random.choice(cards)
    #         user_cards.extend([card1, card2])
    #     else:
    #         card = random.choice(cards)
    #         user_cards.append(card)

    # elif (turn == 'computer'):
    #     if (len(computer_cards) == 0):
    #         card1 = random.choice(cards)
    #         card2 = random.choice(cards)
    #         computer_cards.extend([card1, card2])
    #     else:
    #         card = random.choice(cards)
    #         computer_cards.append(card)

def eleven_checker():
  if(11 in user_cards and sum(user_cards)>21):
    user_cards.remove(11)
    user_cards.append(1)
  elif(11 in computer_cards and sum(computer_cards)>21):
    computer_cards.remove(11)
    computer_cards.append(1)

def black_jack(user_score,computer_score):
    if((user_score==21 and len(user_cards)==2) or (computer_score == 21 and len(computer_cards)==2)):
        print(f"Your final hand:{user_cards},final score:{sum(user_cards)}")
        print(f"Computer's final hand:{computer_cards},final score:{sum(computer_cards)}")
        if (computer_score == 21 and len(computer_cards)==2):
            print("Computer has Blackjack 😱 You lose")
        else:
            print("You has Blackjack 😱 You win")
        return False
    return True


def final_decision(user_score,computer_score):
    if (computer_score > user_score):
        print("You lose😞")
    elif (computer_score < user_score):
        print("You win 🙂")


def decision(user_score,computer_score):
    while computer_score <= 17:
        computer_cards.append(card_choicer())
        eleven_checker()
        computer_score=sum(computer_cards)
    print(f"Your final hand:{user_cards},final score:{user_score}")
    print(f"Computer's final hand:{computer_cards},final score:{computer_score}")
    if (computer_score == user_score):
        print("Match is draw")
        return
    if (user_score > 21):
        print("You went over. You lose😞")
    elif (computer_score > 21):
        print("Computer went over. You win 🙂")
    else:
        final_decision(user_score,computer_score)


# def computer_cards_picker():

end_game = False
while not end_game:
    user_cards = []
    computer_cards = []
    choice = input("Do you want to play a game of Blackjack?'y' or 'n':")
    if (choice == 'y'):
        clear()
        print(logo)
        # user_cards_picker()
        card_picker()
        is_user_choocing = True
        is_user_choocing=black_jack(sum(user_cards),sum(computer_cards))
        while is_user_choocing:
            print(f"Your cards: {user_cards}, current score:{sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            choice = input("Type 'y' to get another card, type 'n' to pass:")
            if (choice == 'y'):
                user_cards.append(card_choicer())
                eleven_checker()
                if (sum(user_cards) > 21):
                    decision(sum(user_cards),sum(computer_cards))
                    is_user_choocing = False
            else:
                decision(sum(user_cards),sum(computer_cards))
                is_user_choocing = False
            # computer_cards_picker()
    else:
        end_game = True

# print(len(user_cards))