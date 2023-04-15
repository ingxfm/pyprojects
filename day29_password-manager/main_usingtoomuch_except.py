import tkinter
import random
from builtins import FileNotFoundError

import pyperclip
# message box does not get imported when we call all classes
# using * because it is another module inside tkinter
from tkinter import messagebox
import json


# ---------------------------- SEARCH ACCOUNT ------------------------------- #
def find_password():
    account = website_entry.get()
    try:
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
        username_data = data[account]["email"]
        password_data = data[account]["password"]
    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found Error",
                               message="No accounts saved.")
    except KeyError:
        messagebox.showwarning(title="No Data Found",
                               message="No details for this website exist.")
    except TypeError:
        messagebox.showwarning(title="No Data Entered",
                               message="Please, enter an account name.")
    else:
        messagebox.showinfo(title=f"Account info: {account}",
                            message=f"Username: {username_data}\n"
                                    f"Password: {password_data}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_creation_god():
    password_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)

    # Show in UI
    password_entry.insert(tkinter.END, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO 1 Create a function called save().
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    data_dict = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields",
                               message="Please, do not leave empty fields.")
    else:
        # is_ok = messagebox.askokcancel(title="Warning", message="Sure?")
        #
        # if is_ok:
        try:
            with open("data.json", "r") as read_file:
                data_read = json.load(read_file)  # Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as write_file:
                json.dump(data_dict, write_file, indent=4)  # Saving data for first time
        else:
            data_read.update(data_dict)  # Updating old data with new data
            with open("data.json", "w") as write_file:
                json.dump(data_read, write_file, indent=4)  # Saving updated data
            print(data_read)
        finally:
            website_entry.delete(0, tkinter.END)
            username_entry.delete(0, tkinter.END)
            username_entry.insert(tkinter.END, "@email.com")
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password manager")
window.config(padx=30, pady=30)

lock_logo = tkinter.PhotoImage(file="logo2.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# TODO Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# TODO Entry boxes
website_entry = tkinter.Entry(width=17)
website_entry.grid(column=1, row=1)
website_entry.focus()  # this method calls the cursor to be located in this entry by default when the app is opened

username_entry = tkinter.Entry(width=41)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(tkinter.END, "@email.com")

password_entry = tkinter.Entry(width=17)
password_entry.grid(column=1, row=3)

# TODO Buttons
generate_password_button = tkinter.Button(text="Generate password",
                                          width=19,
                                          command=password_creation_god)
generate_password_button.grid(column=2, row=3)

add_account_user = tkinter.Button(text="Add", width=36, command=save)
add_account_user.grid(column=1, row=4, columnspan=2)

search_account_button = tkinter.Button(text="Search",
                                          width=10,
                                          command=find_password)
search_account_button.grid(column=2, row=1)

window.mainloop()
