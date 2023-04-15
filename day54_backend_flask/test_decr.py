# def decorator_function(function):  # decorator function
#     def wrapper_function():  # this function calls the function that was passed to the decorator function
#         # we can add things before the function.
#         function()  # this will trigger the function that was passed as argument in the decorator function
#         # function()  # we can execute the function twice by pasting it again or using for/while loops
#         # we can add things after the function.
#     return wrapper_function

from time import sleep

def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        function()
        print('Ahoj!')
    return wrapper_function


# @delay_decorator
def say_gym():
    print('gym!')

def say_damn():
    print('damn!')

# say_gym()


decorated_function = delay_decorator(say_gym)
decorated_function()
