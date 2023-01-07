#Step 5
from replit import clear
import random
from hangman_art import stages,logo
from hangman_words import word_list

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "b_artaboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    # in_the_list=False

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    if guess in display:
      print("You have already guessed this word")
    else:
      for idx in range(0,len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx]=guess
            # in_the_list=True

    #Check if user is wrong.
    if guess not in chosen_word:
      lives-=1;
      print(f"You guessed {guess} that's not ture so you lose one life")
    if(lives==0):
      print("You lose")
      end_of_game=True

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])