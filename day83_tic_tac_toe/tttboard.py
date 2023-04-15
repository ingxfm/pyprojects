# VIEW from MVC architecture

ZERO_INDEXING = 1


class GameBoard:

    def __init__(self, rows):
        self.rows = rows
        self.art: str = f'''
                       |   |   
                     {self.rows[6]} | {self.rows[7]} | {self.rows[8]}             
                    ___|___|___
                       |   |   
                     {self.rows[3]} | {self.rows[4]} | {self.rows[5]} 
                       |   |   
                    ¯¯¯|¯¯¯|¯¯¯
                     {self.rows[0]} | {self.rows[1]} | {self.rows[2]}
                       |   |   
                    '''
        self.controls = '''Controls:
        7 | 8 | 9
        4 | 5 | 6
        1 | 2 | 3  
        '''

    def add_position(self, choice, symbol):
        self.rows[choice - ZERO_INDEXING] = symbol
        self.art: str = f'''
                       |   |   
                     {self.rows[6]} | {self.rows[7]} | {self.rows[8]}             
                    ___|___|___
                       |   |   
                     {self.rows[3]} | {self.rows[4]} | {self.rows[5]} 
                       |   |   
                    ¯¯¯|¯¯¯|¯¯¯
                     {self.rows[0]} | {self.rows[1]} | {self.rows[2]}
                       |   |   
                    '''

