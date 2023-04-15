import pandas as pd
from turtle import Turtle, Screen

IMAGE = "europe.gif"
DATA_FILE = "european_countries.csv"
FONT = ("Arial", 8, "normal")
ALIGNMENT = "center"

screen = Screen()
screen.title("Europe map")
screen.addshape(IMAGE)
Turtle(shape=IMAGE)
screen.tracer(0)


def play_game():
    data = pd.read_csv(DATA_FILE)
    states = data.state.to_list()
    are_states_undiscovered = 1
    count = 0
    total_count = data.state.count()
    print(count)
    guessed_states = []

    while are_states_undiscovered:
        state_name = screen.textinput(f"{count}/{total_count} - Name-a-State", "Please, enter the name of a state:")
        screen.update()
        if state_name.title() in states:
            count += 1
            guessed_states.append(state_name.title())
            state_info = data[data.state == state_name.title()]
            new_state = Turtle()
            new_state.hideturtle()
            new_state.color("red")
            new_state.penup()
            new_state.goto(int(state_info.x), int(state_info.y))
            new_state.write(f"{state_name.title()}", align=ALIGNMENT, font=FONT)
            states.remove(state_name.title())
        elif state_name.title() == "Exit":
            are_states_undiscovered = 0
            pd.DataFrame(states).to_csv("states_to_learn.csv")
        if count == total_count:
            are_states_undiscovered = 0
            continue_gaming = screen.textinput("Do you want to play again?")
            if continue_gaming == "y":
                play_game()


play_game()
screen.exitonclick()

#  missing_states = [state for state in all_states if state not in guessed_states]

#  new_dict = {new_key: new_value for item in list}
#  new_dict = {new_key: new_value for (key, value) in dict.items()}

#  new_dict = {new_key: new_value for item in list if test}
#  new_dict = {new_key: new_value for (key, value) in dict.items() if test}