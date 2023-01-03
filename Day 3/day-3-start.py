print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0;

if height>=120:
  print("You can ride the rollercoaster");
  age = int(input("Enter your age:"))
  if age<12:
    bill=5
    print("You have to pay $5.")
  elif age<=18:
    bill=7
    print("You have to pay $7.")
  elif age>=45 and age<=55:
    print("you have free tickets")
  else:
    bill=12
    print("You have to pay $12")
  wants_photo=input("Do you want a photo?")
  if wants_photo=='y':
    bill+=3;
  print(f"you have to pay {bill}")
else:
  print("Sorry, you have to grow taller before you can ride")

