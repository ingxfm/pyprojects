class Dog:
    # In this example, the class Dog will be the super class.
    # It is the "mother" class from which we are inheriting.
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    # In this example, the class Labrador is the sub-class.
    # It is the "daughter" class that inherits.
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True

    def bark(self):
        # super is used when we want to inherit
        # the characteristics from the super class
        super().bark()
        print("Greetings, good sir. How do you do?")


sparky = Labrador()
sparky.bark()
