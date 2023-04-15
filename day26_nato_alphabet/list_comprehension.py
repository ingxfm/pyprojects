# #  NO list comprehension
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# print(new_list)

#  with list comprehension
# numbers = [1, 2, 3]
# # new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Juaniquito Perez"
# new_list = [letter for letter in name]
# print(new_list)
# new_string = letter for letter in name  # It does not work.
# print(new_string)

# # TODO Create a new list from a range, where the list items are double the values in the range.
# range_list = [2*number for number in range(1, 5)]
# print(range_list)

# # TODO Create a new list that contains the names longer than 5 characters in ALL CAPS.
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 4]
# print(new_list)


#  missing_states = [state for state in all_states if state not in guessed_states]

#  new_dict = {new_key: new_value for item in list}
#  new_dict = {new_key: new_value for (key, value) in dict.items()}

#  new_dict = {new_key: new_value for item in list if test}
#  new_dict = {new_key: new_value for (key, value) in dict.items() if test}

