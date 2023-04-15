from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system, name
from time import sleep

# TODO 1 Print report
# TODO 2 Check resources are sufficient
# TODO 3 Process coins
# TODO 4 Check transactions are successful
# TODO 5 Make coffee


clearConsole = lambda: system('cls' if name in ('nt', 'dos') else 'clear')


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = 1
# step 1
while machine_on:
    wish = input(f"What would you like? ({menu.get_items()}): ")
    if wish == "e":
        wish = "espresso"
        drink = menu.find_drink(wish)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    elif wish == "l":
        wish = "latte"
        drink = menu.find_drink(wish)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    elif wish == "k":
        wish = "cappuccino"
        drink = menu.find_drink(wish)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    elif wish == "r":
        coffee_maker.report()
        money_machine.report()  # step 3
    elif wish == "off":
        print("Good bye.")
        machine_on = 0  # step 2
    else:
        print("Invalid entry. Please, type 'e' for espresso, 'l' for latte, or 'k' for cappuccino.\n")
    sleep(3)
    clearConsole()
