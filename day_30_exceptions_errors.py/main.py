# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["ssssss"])
# except FileNotFoundError:
#     print("no no no")
#     open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
# finally:
#     file.close()
#     print("File was closed.")
#     raise KeyError("I created this error.")

# Notes: do not use a bare except.
# else will execute only if all lines of code in try are
# successful. If any line in the try fails, then it won't
# be executed.
# finally executes no matter what

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("This height is not possible in a human being.")
