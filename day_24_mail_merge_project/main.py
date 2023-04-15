# TODO: Create a letter using starting_letter.txt
#  for each name in invited_names.txt
#  Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend".

# Hint1: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
STARTING_FIRST_LINE = "Dear [name],\n"

with open(r".\Input\Letters\starting_letter.txt") as file:
    lines_list_in_starting_letter = file.readlines()

with open(r".\Input\Names\invited_names.txt") as file:
    names_list = file.readlines()

for name in names_list:
    file_name = name.strip("\n")
    new_first_line = lines_list_in_starting_letter[0].replace(PLACEHOLDER, file_name)
    lines_list_in_starting_letter[0] = new_first_line

    with open(r"./Output/ReadyToSend/{name}.txt".format(name=file_name), mode="w") as file:
        for line in lines_list_in_starting_letter:
            file.write(f"{line}")
    lines_list_in_starting_letter[0] = STARTING_FIRST_LINE
