from menu import MENU, resources
from os import system, name
from time import sleep

current_resources = resources

clear = lambda: system("cls" if name == "n" else "clear") or None


# TODO: 7. Make Coffee. DONE
def make_coffee(order, resources_info):
    '''    Subtracts the magnitudes of the ingredients
    of your wish to the total in the machine.    '''
    for resource in resources_info:
        resources_info[resource] = resources_info[resource] - MENU[order]["ingredients"][resource]
    print(f"\nHere is your {order} ☕. Enjoy :D ! \n")
    print(f"Here are the current resources:\n"
          f"Water: {resources_info['water']}ml\n"
          f"Milk: {resources_info['milk']}ml\n"
          f"Coffee: {resources_info['coffee']}g\n")
    return resources_info


# TODO: 3. Print report
def report(resources_info, money_gained):
    return f"Water: {resources_info['water']}ml\n" \
           f"Milk: {resources_info['milk']}ml\n" \
           f"Coffee: {resources_info['coffee']}g\n" \
           f"Money: ${money_gained:.2f}"


# TODO: 5. Process coins.
def payments(order, resources_info, cost):
    change = 0
    print(f"\nPlease enter coins, only. The cost is ${cost:.2f}.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    sum_entered = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    change = sum_entered - cost
    if change < 0:
        return change
    else:
        print(f"The amount inserted is ${sum_entered:.2f}.")
        print(f"The change is ${change:.2f}.")
        return change


# TODO: 4. Check resources sufficient?
#  resources dict is the maximum amount for the machine
# TODO: 6. Check transaction successful?
def check_resources(order, resources_info):
    water_cond: bool = resources_info["water"] >= MENU[order]["ingredients"]["water"]
    milk_cond: bool = resources_info["milk"] >= MENU[order]["ingredients"]["milk"]
    coffee_cond: bool = resources_info["coffee"] >= MENU[order]["ingredients"]["coffee"]
    if water_cond and milk_cond and coffee_cond:
        # print("\nIt reached resources.\n")
        change_out_function = 1
        attempts = 0
        while change_out_function:
            # clear()
            costing_var = payments(order, resources_info, MENU[order]["cost"])
            attempts += 1
            if costing_var >= 0:
                change_out_function = 0
                ri = make_coffee(order, resources_info)
                return ri
            elif attempts > 1:
                change_out_function = 0
            clear()
    elif not water_cond:
        print("Sorry there is not enough water. Money refunded. Add water or request another option.\n")
        return resources_info
    elif not milk_cond:
        print("Sorry there is not enough milk. Money refunded. Add milk or request another option.\n")
        return resources_info
    elif not coffee_cond:
        print("Sorry there is not enough coffee. Money refunded. Add coffee or request another option.\n")
        return resources_info


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”
#  E for espresso, L for latte, K cappuccino, R for report
# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt and
#  repeat the process to server the next customer
is_game_over: int = 0  # 0 is False, 1 is True.
money = 0
while not is_game_over:
    your_wish: str = input("What would you like? (espresso/latte/cappuccino).\n"
                           "Type E for espresso, L for latte, K cappuccino:").lower()
    if your_wish == "e":
        your_wish = "espresso"
        current_resources = check_resources(your_wish, current_resources)
        money += MENU[your_wish]["cost"]
    elif your_wish == "l":
        your_wish = "latte"
        current_resources = check_resources(your_wish, current_resources)
        money += MENU[your_wish]["cost"]
    elif your_wish == "k":
        your_wish = "cappuccino"
        current_resources = check_resources(your_wish, current_resources)
        money += MENU[your_wish]["cost"]
    elif your_wish == "r":
        print(report(current_resources, money))
    elif your_wish == "off":
        print("The machine is turning off. Good bye.")
        is_game_over = 1
    else:
        print("Invalid entry. Type E for espresso, L for latte, K cappuccino.")
    sleep(3)
    clear()

