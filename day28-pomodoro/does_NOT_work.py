check_marks = [0, 0, 0, 0]

for check_mark in check_marks:
    print(check_mark)
    check_mark = tkinter.Label(text="✔", bg=YELLOW, fg=RED)
    column = 1
    check_mark.grid(column=column, row=3)
    column += 1
    print(check_mark)

# my code
if reps == 1 or reps == 3 or reps == 5 or reps == 7:
    timer_countdown(work_seconds)
elif reps == 2 or reps == 4 or reps == 6:
    timer_countdown(short_break_seconds)
elif reps == 8:
    timer_countdown(long_break_seconds)

# her code is better
if reps % 8 == 0:
    timer_countdown(long_break_seconds)
elif reps % 2 == 0:
    timer_countdown(short_break_seconds)
else:
    timer_countdown(work_seconds)
