MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def check_resources(coffee):
    # You can loop through dictionary of ingredients and check for this rather than doing this and for this i should use
    # my menu instead of resources
    if (coffee == "latte" or coffee == "cappuccino"):
        if (resources['milk'] < MENU[coffee]["ingredients"]['milk']):
            print("Sorry there is not enough Milk.")
            return False
    if (resources['water'] < MENU[coffee]["ingredients"]['water']):
        print("Sorry there is not enough Water.")
        return False
    elif (resources['coffee'] < MENU[coffee]["ingredients"]['coffee']):
        print("Sorry there is not enough Coffee.")
        return False
    else:
        return True


def coin_manager():
    # i should use total + in each statement because it does not going to maater
    quarters = int(input("Enter quarters:"))
    dimes = int(input("Enter dimes:"))
    nickles = int(input("Enter nickles:"))
    pennies = int(input("Enter pennies:"))

    final_coins = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    return final_coins


def reduce_resources(coffee, ingredients):
    # you can use loop through for this and use menu ingredients instead of resources
    # for item in ingredients:                                                                                              
    #     ingredients[item]-=MENU[coffee]['ingredients'][item]                                                                  
    resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']
    if (coffee == "latte" or coffee == "cappuccino"):
        resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']
    return ingredients


def coins_checker(coins, coffee, money):
    # here need only two conditions one for >= and else in  >= we can get change and we can add money from our menu cost
    if (MENU[coffee]["cost"] == coins):
        money += coins
    elif (coins > MENU[coffee]["cost"]):
        change = round((coins - MENU[coffee]["cost"]), 2)
        money = money + (coins - change)
        print(f"Here is ${change} dollars in change.")
    elif (MENU[coffee]["cost"] > coins):
        print("Sorry that's not enough money. Money refunded.")
    return round(money,2)


# def produce_coffee(coffee):
#     if(check_resources(coffee)):
#         return True
#     else:
#         print("Sorry,There is not sufficient resoures for making espresso")
#         return False

# def produce_latte():
#     if (check_resources("latte")):
#         print("coffee is making...")
#     else:
#         print("Sorry,There is not sufficient resoures for making latte")

# def produce_cappuccino():
#     if (check_resources("cappuccino")):
#         print("coffee is making...")
#     else:
#         print("Sorry,There is not sufficient resoures for making cappuccino")

def userchoice(money, resources):
    running_maching = True
    while running_maching:
        choice = input("What would you like(espresso,latte,cappuccino)?").lower()
        if (choice == "report"):
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif (choice == "espresso" or choice == "latte" or choice == "cappuccino"):
            if (check_resources(choice)):
                coins = coin_manager()
                old_money = money
                money = coins_checker(coins, choice, money)
                if (money > old_money):
                    print(f"Here is your {choice}. Enjoy!")
                    resources = reduce_resources(choice, resources)
        elif (choice == "off"):
            running_maching = False
        else:
            print("Enter valid input")


userchoice(money, resources)
