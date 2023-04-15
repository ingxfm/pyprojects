import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


want_a_band_name = True
while want_a_band_name:
    clear_screen()
    print('Welcome to the name band generator.')
    city_name = input('what is the name of the city you grew up in?')

    pet_name = input('what is your pet\'s name?')

    print(f'Your band\'s name could be {city_name} {pet_name}.'
          f'This name has {len(city_name+pet_name)} characters.\n')

    continue_naming = input('Do you want another option to name your band? Type \'Y\' for yes: ').lower()

    if not continue_naming != 'y':
        break
