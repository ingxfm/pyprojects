# MODEL from MVC architecture

class Player:

    def __init__(self, symbol):
        self.symbol = symbol
        self.play: str = ''

    def your_turn(self):
        self.play = input('Press a number key from 1 to 9 to select a position: ')


