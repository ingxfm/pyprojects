
#
# def processing_wish(order):
#     if order == "espresso":
#         # call function for espresso
#     elif order == "latte":
#         # call function for latte
#     elif order == "cappuccino":
#         # call function for cappuccino
#     elif order == "report":
#         # call function for report
#     elif order == "off":
#         # call function to turn off the machine
#     else:
#         print("Invalid entry. Please try again.")
#         #call function to your_wish again
#
#
#
# TODO Compare the code above VS this code below that substitute the code in the
#  file main.py around lines 21 to 46.

def make_coffee(order):
    '''Subtracts the magnitudes of the ingredients of your wish to the total in the machine'''
    return f"Here is your {order}."


# # # TODO: 3. Print report
def report():
    # print(resources)
    return f"Water: {resources['water']}\n " \
           f"Milk: {resources['milk']}\n " \
           f"Coffee: {resources['coffee']}\n"


def turn_off_machine():
    return "The machine is turning off. Good bye."


options = {
    "espresso": make_coffee(your_wish),
    "latte": make_coffee(your_wish),
    "cappuccino": make_coffee(your_wish),
    "report": report(),
    "off": turn_off_machine(),
}

print(options[your_wish])

#is it possible to call these functions without them executing
#investigate and get deeper with invoking functions without parentheses