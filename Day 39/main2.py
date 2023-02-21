from data_manager import DataManager

first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
email = input("Enter your email:")
email2 = input("Enter your email again:")
if (email == email2):
  data_manager = DataManager()
  data_manager.put_users(first_name, last_name, email)
  print("You are a part of us now")
else:
  print("Two emails are not match")
