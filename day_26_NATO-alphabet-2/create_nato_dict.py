import pandas as pd


nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def translate_to_NATO_alphabet():
    try:
        name = input("Enter a name: ").upper()
        natify = [nato_dict[item] for item in name]
    except KeyError:
        print("Please, enter letter from the NATO alphabet.")
        translate_to_NATO_alphabet()
    else:
        print(natify)


translate_to_NATO_alphabet()
