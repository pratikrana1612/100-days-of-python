import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list=[rock,paper,scissors]
choice=input("what do you want to choose Rock,Paper,Scissors?").lower()

if(choice=='rock'):
  choice=0
elif(choice=='paper'):
  choice=1
else:
  choice=2

computer_choice=random.randint(0,2)

print(list[choice])
print("Computer Choice:")
print(list[computer_choice])



if(choice==computer_choice):
  print("Match is draw")
elif(choice==1 and computer_choice==0):
  print("You win")
elif(choice==0 and computer_choice==2):
  print("You win")
elif(choice==2 and computer_choice==1):
  print("You Win")
else:
  print("You lose")
  
# if((choice+1)%3==computer_choice):
#   print("You lose")
# elif(choice==computer_choice):
#   print("Match draw")
# else:
#   print("You win")



