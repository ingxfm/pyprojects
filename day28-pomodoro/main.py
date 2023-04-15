import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_POS_X = 102
CANVAS_POS_Y = 112
CANVAS_TEXT_POS_Y = 132
CANVAS_SIZE_X = 200
CANVAS_SIZE_Y = 224
PADDING = 100
STARTING_TIME = "00:00"
STARTING_COUNT = 1  # minutes
job_timer_countdown = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(job_timer_countdown)
    canvas.itemconfig(timer_text, text=STARTING_TIME)
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        title_label.config(text="Work", fg=GREEN)
        timer_countdown(work_seconds)
    elif reps == 2 or reps == 4 or reps == 6:
        title_label.config(text="Short Break", fg=PINK)
        timer_countdown(short_break_seconds)
    elif reps == 8:
        title_label.config(text="Long Break", fg=RED)
        timer_countdown(long_break_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_countdown(counting):
    minutes_left = math.floor(counting / 60)
    seconds_left = int(counting % 60)
    canvas.itemconfig(timer_text, text=f"{minutes_left}:{seconds_left:02d}")
    if counting > 0:
        global job_timer_countdown
        # this takes positional arguments after taking a function as argument
        # after taking a time in milliseconds
        job_timer_countdown = window.after(1000, timer_countdown, counting - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for item in range(work_sessions):
            mark += "✔"
            check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=PADDING, pady=PADDING, bg=YELLOW)

# a way to read an image
tomato_image = tkinter.PhotoImage(file="tomato.png")
# widget canvas allows to layer things one of top of the other.
# highlightthickness = 0 to remove line between background and
# the alpha channel of the image
canvas = tkinter.Canvas(width=CANVAS_SIZE_X, height=CANVAS_SIZE_Y, bg=YELLOW)
# reading the image and giving center coordinates of it.
# coordinates I gave are half of width and height
canvas.create_image(CANVAS_POS_X, CANVAS_POS_Y, image=tomato_image)
timer_text = canvas.create_text(CANVAS_POS_X,
                                CANVAS_TEXT_POS_Y,
                                text=STARTING_TIME,
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,
                            font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.config(padx=5, pady=1)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.config(padx=5, pady=1)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text="", bg=YELLOW, fg=RED)
check_marks.grid(column=1, row=3)


window.mainloop()
