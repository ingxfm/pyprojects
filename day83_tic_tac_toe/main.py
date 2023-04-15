# built-in
from os import system, name

# 3rd-party

# my-own
from tttboard import GameBoard
from art import logo, EMPTY_CELLS

# CONTROLLER from MVC architecture

players_positions: dict = {'x': [],
                           'o': []}

initial_board: GameBoard = GameBoard(rows=EMPTY_CELLS)


def clear_console():
    system('cls' if name == 'nt' else 'clear')
    print('\n\n--------------------\nIt should be cleared.\n--------------------')


def is_there_a_winner(positions: dict, current_player):
    winning_combinations = [(1, 5, 9),
                            (3, 5, 7),
                            (1, 2, 3),
                            (4, 5, 6),
                            (7, 8, 9),
                            (1, 4, 7),
                            (2, 5, 8),
                            (3, 6, 9)]

    for combination in winning_combinations:
        if all(item in positions[current_player] for item in combination):
            return True
    return False

def check_draw(positions: dict, current_player):
    if len(positions['x']) + len(positions['o']) == 9:
        return True
    return False



def play_tic_tac_toe():
    print(initial_board.controls, end=' ')
    choice = input('Please choose "x" or "o", the 2nd player will have the other symbol: ')
    if choice == 'x':
        symbols: list = ['x', 'o']
    else:
        symbols: list = ['o', 'x']

    print(initial_board.art)

    playing = True
    turns_passed: int = 0
    played_positions: list = []
    while playing:
        try:
            for symbol in symbols:
                player_choice = int(input('Press a key from 1 to 9 to select a cell: '))

                if player_choice not in played_positions:
                    players_positions[symbol].append(player_choice)
                    clear_console()
                    print(logo)
                    print(initial_board.controls)
                    print(players_positions)
                    initial_board.add_position(choice=player_choice, symbol=symbol)
                    print(players_positions)
                    print(initial_board.art)
                    played_positions.append(player_choice)
                    turns_passed += 1
                    if turns_passed > 4:
                        winner = is_there_a_winner(positions=players_positions, current_player=symbol)
                        if winner:
                            return f'Player "{symbol}" wins.'
                        draw = check_draw(positions=players_positions, current_player=symbol)
                        if draw:
                            return 'Draw!'

                else:
                    print(symbols)
                    symbols = symbols[::-1]  # this invert the list in the for loop
                    print(symbols)
                    print('Choose another position')

        except TypeError as TE:
            print(f'{TE}.\nPlease only enter numbers from 1 to 9.')

        except ValueError as VE:
            print(f'{VE}.\nPlease only enter numbers from 1 to 9.')




play_game = True
while play_game:
    play_game = input('Do you want to play Blackjack? Type "y" for yes or "n" for no: ')
    if play_game == 'n':
        play_game = False
        print('Good bye!')
    else:
        clear_console()
        print(logo)
        result = play_tic_tac_toe()
        print(result)
