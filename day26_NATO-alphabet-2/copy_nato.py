import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

# print(nato_alphabet)

# Loop through rows of a data frame
for (index, row) in nato_alphabet.iterrows():
    #Access index and row
    # print(row.student)
    #Access row.student or row.score
    # print(row.score)
    pass

#  missing_states = [state for state in all_states if state not in guessed_states]

#  new_dict = {new_key: new_value for item in list}
#  new_dict = {new_key: new_value for (key, value) in dict.items()}

#  new_dict = {new_key: new_value for item in list if test}
#  new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Looping through a dictionary
# for (key, value) in dict.items():
#     print(key, value)

# Looping through a Pandas dataframe
# for (key, value) in dataframe.items():
#     print(key, value)

# Looping through a rows of a dataframe
# for (index, row) in dataframe.iterrows():
#     print(key, value)

# get a particular single value (a cell) from the dataframe
# monday = dataframe[dataframe.day == "Monday"]
# print(monday.condition)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_dict)

# her code is the same sa mine


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a name: ").upper()
natify = [nato_dict[item] for item in name if item in nato_dict.keys()]
print(natify)

# her code is better
# word = input("Enter a word: ").upper()
# output_list = [nato_dict[letter] for letter in word]
