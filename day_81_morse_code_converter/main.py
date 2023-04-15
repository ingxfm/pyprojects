MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '       ', }


def get_word():
    word = input('Please enter a word: ')
    return word


def morse_translator(word):
    word_in_morse_list = []
    for letter in word:
        if letter.upper() in MORSE_CODE_DICT:
            word_in_morse_list.append(MORSE_CODE_DICT[letter.upper()])
            word_in_morse_str: str = '   '.join(word_in_morse_list)  # Morse words are separated by 3 dits
        else:
            print('Please, do not enter special characters.')
            morse_translator()

    if word_in_morse_str:
        print(word_in_morse_str)


to_continue = True

while to_continue:
    try:
        morse_translator(word=get_word())

    except TypeError as TE:
        print('There is unknown characters in the text')

    entering_words = input('\nDo you want to continue? Please, enter Y or N, for Yes or Not: ')

    if entering_words.upper() == 'N':
        to_continue = False


