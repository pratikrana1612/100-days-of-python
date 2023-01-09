from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret ouction program.")

bidders={}
endgame=False
def highest_bidder():
  max=0;
  for key in bidders:
    if(bidders[key]>max):
      max=bidders[key]
      name=key
  print(f"The winner is {name} with a bid of {max}")

  
while not endgame:
  name=input("What is your name?")
  bid=int(input("What's your bid?$"))
  bidders[name]=bid
  choice=input("Are there any other bidders?'yes' or 'no'")
  if(choice=='no'):
    endgame=True;
    highest_bidder()
  else:
    clear()
  