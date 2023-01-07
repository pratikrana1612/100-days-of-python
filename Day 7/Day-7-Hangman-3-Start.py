#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
whole_word=[]
for ch in chosen_word:
    whole_word.append("_")
print(whole_word)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


#Check guessed letter
end_of_game=False
# while '_' in whole_word:
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  for idx in range(0,len(chosen_word)):
      if chosen_word[idx] == guess:
          whole_word[idx]=guess
  print(whole_word)

  if '_' not in whole_word:
    end_of_game=True;
    print("You Won!")
