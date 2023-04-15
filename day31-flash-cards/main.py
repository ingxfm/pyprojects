import tkinter
import pandas as pd
import random
from time import sleep

# ---------------------------- CONSTANTS ------------------------------- #
WIDTH_BACKGROUND = 800
HEIGHT_BACKGROUND = 526
POSITION_BACKGROUND_X = int(WIDTH_BACKGROUND/2)
POSITION_BACKGROUND_Y = int(HEIGHT_BACKGROUND/2)
BACKGROUND_COLOR = "#B1DDC6"
WIDTH_FOREGROUND = 800
HEIGHT_FOREGROUND = 526
POSITION_FOREGROUND_X = int(WIDTH_FOREGROUND/2)
POSITION_FOREGROUND_Y = int(HEIGHT_FOREGROUND/2)
FONT_QUESTION = ("Courier", 20)
FONT_ANSWER = ("Courier", 40, "bold")
new_card_dict = {}
job_timer_countdown = None

# ---------------------------- READ CSV ------------------------------- #
try:
    original_word_list = pd.DataFrame.to_dict(pd.read_csv("data/words_to_learn.csv"), orient="records")
except FileNotFoundError:
    original_word_list = pd.DataFrame.to_dict(pd.read_csv("data/french_words.csv"), orient="records")


# ---------------------------- RANDOM WORD ------------------------------- #
def random_word():
    global original_word_list, new_card_dict, job_timer_countdown
    window.after_cancel(job_timer_countdown)
    new_card_dict = random.choice(original_word_list)
    new_question = new_card_dict["French"]

    canvas_card_front.itemconfig(language_text, text="French", fill="black")
    canvas_card_front.itemconfig(trainings_text, text=new_question, fill="black")
    canvas_card_front.itemconfig(canvas_image, image=card_front_img)
    job_timer_countdown = window.after(3000, answering)


# ---------------------------- ANSWER ------------------------------- #
def answering():
    new_answer = new_card_dict["English"]
    canvas_card_front.itemconfig(canvas_image, image=card_back_img)
    canvas_card_front.itemconfig(language_text, text="English", fill="white")
    canvas_card_front.itemconfig(trainings_text, text=new_answer, fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #
def is_known():
    original_word_list.remove(new_card_dict)
    print(len(original_word_list))
    data = pd.DataFrame(original_word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_word()


# ----------------------------  UI  ------------------------------- #
window = tkinter.Tk()
window.title("Flash card software")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)

job_timer_countdown = window.after(3000, answering)

# background
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
canvas_card_front = tkinter.Canvas(width=WIDTH_FOREGROUND, height=HEIGHT_BACKGROUND, highlightthickness=0)
canvas_image = canvas_card_front.create_image(POSITION_FOREGROUND_X, POSITION_FOREGROUND_Y, image=card_front_img)
canvas_card_front.config(bg=BACKGROUND_COLOR)
language_text = canvas_card_front.create_text(400, 150, text="", fill="black", font=FONT_QUESTION)
trainings_text = canvas_card_front.create_text(400, 263, text="", fill="black", font=FONT_ANSWER)
canvas_card_front.grid(column=0, row=0, columnspan=2)
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")

# buttons
image_right = tkinter.PhotoImage(file="images/right.png")
button_right = tkinter.Button(image=image_right, command=is_known, highlightthickness=0)
button_right.grid(column=1, row=1)
print(button_right)

image_wrong = tkinter.PhotoImage(file="images/wrong.png")
button_wrong = tkinter.Button(image=image_wrong, command=random_word, highlightthickness=0)
button_wrong.grid(column=0, row=1)
print(button_wrong)

# job_timer_countdown = window.after(3000, random_word)
random_word()

window.mainloop()