from tkinter import *

FONT = ("Arial", 20, "bold")


def button_clicked():
    print("I got clicked")
    new_text = input_entry.get()
    my_label.config(text=new_text)


window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# parameters can be not specified in the function comments
my_label = Label(text="I'm a Label", font=FONT)
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.pack()  # pack places on top, center, left, right, bottom
# my_label.place(x=0, y=0)  # specific coordinate
my_label.grid(column=0, row=0)  # use columns and rows

# button
button = Button(text="Click Me", command=button_clicked)
# button.pack()  # pack places on top, center, left, right, bottom
button.grid(column=1, row=1)

# entry component
input_entry = Entry(width=10)
# input_entry.pack()  # pack places on top, center, left, right, bottom
input_entry.grid(column=3, row=2)

# new button
new_button = Button(text="2nd option")
new_button.grid(column=2, row=0)
# she calls padding to the margins to widgets

window.mainloop()
