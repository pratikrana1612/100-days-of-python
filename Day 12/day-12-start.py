################### Scope ####################

enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# def game():
#   def drink_potion():
#     potion_strength=2;
#     print(potion_strength)
#   drink_potion()

# game()
# # drink_potion()
# # print(potion_strength)
# game_level=3
# enemies=["p","q","r"]
# def new_enemies():
#   if game_level<5:
#     new_enemy=enemies[0]

# print(new_enemy)
def increase_enemies():
  # global enemies
  # enemies=2
  # print(enemies)
  return enemies +1 
enemies=increase_enemies()
print(enemies)

# global constants


PI=3.14
# URLS OF WEBSITES
# you don't have to write global to read the global varibale or print the global variable if you want to write the only you have to use global inside 
# function
def fun():
  print(PI)

fun()