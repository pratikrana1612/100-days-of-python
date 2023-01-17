from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# drink=MenuItem()
is_running = True

while is_running:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if (choice == 'report'):
        coffee_maker.report()
        money_machine.report()
    elif (choice == 'off'):
        is_running = False
    else:
        drink = menu.find_drink(choice)
        # print(drink.ingredients)
        # print(drink.name,drink.cost)
        if (coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)
