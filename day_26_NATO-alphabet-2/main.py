student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
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

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
{new_key:new_value for (index, row) in student_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

