class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        # temperament declared in this class overrides the inherited temperament
        self.temperament = "guay"


san = Labrador()
print(san.temperament)

# Reference:
# https://stackoverflow.com/questions/27826095/what-is-the-difference-between-super-being-called-at-the-beginning-or-end-of-a