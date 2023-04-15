

def two_digit_func():
    two_digit_number = int(input('Enter a 2-digit number: '))

    if two_digit_number < 10 or two_digit_number > 99:
        print('Please, enter a number between 10 and 99 (both limits included).')
        two_digit_func()
    return two_digit_number


def add_number_parts(two_digit_number):
    tenth = int(two_digit_number/10)
    unit = two_digit_number - (tenth*10)
    addition = tenth + unit
    return addition




continue_playing = True
while continue_playing:
    two_digits_num = two_digit_func()
    resultat = add_number_parts(two_digit_number=two_digits_num)
    print(f'The original number is {two_digits_num} and the component addition is {resultat}.')
    choice = input('Do you want to continue playing? If Yes, enter "y": ').lower()
    if choice != 'y':
        break
