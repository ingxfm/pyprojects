import tkinter

FONT = ("Arial", 10, "bold")

window = tkinter.Tk()
window.title("Miles (mi) to Kilometers (km)")
window.minsize(width=100, height=100)


def miles_2_km():
    miles_value = input_entry.get()
    result = int(miles_value) * 1.6
    label_result_km.config(text=f"{result}")


label_equal_to = tkinter.Label(text="is equal to", font=FONT)
label_equal_to.grid(column=0, row=2)

label_miles = tkinter.Label(text="miles", font=FONT)
label_miles.grid(column=3, row=2)

label_km = tkinter.Label(text="km", font=FONT)
label_km.grid(column=2, row=3)

label_result_km = tkinter.Label(text="0", font=FONT)
label_result_km.grid(column=1, row=3)

# button
button = tkinter.Button(text="Calculate", command=miles_2_km)
# button.pack()  # pack places on top, center, left, right, bottom
button.grid(column=1, row=2)

input_entry = tkinter.Entry(width=10)
# input_entry.pack()  # pack places on top, center, left, right, bottom
input_entry.grid(column=1, row=1)

window.mainloop()