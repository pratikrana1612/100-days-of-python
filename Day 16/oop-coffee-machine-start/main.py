from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffeemaker=CoffeeMaker()
menuitem=MenuItem()
isrunning=True
while isrunning:
    menuitem.name=input(f"What would you like? {menu.get_items()}: ")
    if(menuitem=="report"):
        print(coffeemaker.report())
    elif(menuitem=="off"):
        isrunning=False
    else:
        if(coffeemaker.is_resource_sufficient(menuitem.name)):
            make_payment()
        else:
            print("Resources are insufficient")