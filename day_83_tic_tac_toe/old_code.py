# built-in
from os import system, name

# 3rd-party

# My own
from player_class import Player
from art import logo
from tttboard import GameBoard

first_line = [1, 2, 3]
second_line = [4, 5, 6]
third_line = [7, 8, 9]

# player_x = Player('x')
# player_o = Player('o')
board = GameBoard(row_1=first_line, row_2=second_line, row_3=third_line)


def clear_console():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def tic_tac_toe():
    print('To play TTT (tic-tac-toe), press a number from 1 to 9.\n'
          'From 1 to 3, for the first line, from left to right.\n'
          'From 4 to 6, for the second line, from left to right.\n'
          'From 7 to 9, for the third line, from left to right.\n')

    play = input('Press a number key from 1 to 9 to select a position: ')

    if play:
        print(board.game_board())

    # for key in controls:
    #     if int(play) in controls[key]:
    #         controls[key][controls[key].index(int(play))] = player_x.symbol
    #         for key in controls:
    #             print(f'{controls[key]}')
    #         print('yeah')


play_game = True
while play_game:
    play_game = input('Do you want to play Blackjack? Type "y" for yes or "n" for no: ')
    if play_game == 'n':
        play_game = False
        print('Good bye!')
    else:
        clear_console()
        print(logo)
        tic_tac_toe()
