# # to create a custom class
# # 1st do the definition of the class
# # First letter of each word is capitalized
# # PascalCase vs camelCase vs snake_case
# class User:
#     #what they have
#     #what they can do
#     pass
#
# # 2nd, build an object from that class
# user_1 = User()
# # An attribute is a variable associated with a class
# user_1.id = "001"
# user_1.username = "Juan"
#
# # A constructor is a way specify starting pieces of information
# # for object of a class. What should happen when an object
# # is bring constructed? Initializing: specifying variables
# # or counters with their starting values. And to clear from
# # previous data.
# # __init__ initializes all attributes. And it is called every
# # time we will create an object from the said class.
# # self is the actual object that is being initialized
# # as many parameters as desired can be added
#
#
# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
# my_car = Car(5) # my_car.seats = 5
# # This above is the same as if we would first create the
#


class User:
    #  attributes
    def __init__(self, user_id, username):  # usually the name of the parameter
        # is equal to the name of the attribute
        # but is not a must
        self.id = user_id
        self.username = username
        self.followers = 0  # setting a default value
        self.following = 0

    def follow(self, user):  # methods always have self parameter,
        # so they know what was the object that called it.
        user.followers += 1
        self.following += 1


user_1 = User("001", "Juan")
user_2 = User("002", "Kloaka")
print(f"Before: {user_2.followers}")
user_1.follow(user_2)
print(user_1.id)
print(f"After: {user_2.followers}")