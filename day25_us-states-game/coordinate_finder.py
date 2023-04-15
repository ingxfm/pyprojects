from turtle import Turtle, Screen
import pandas as pd

IMAGE = "europe.gif"

screen = Screen()
screen.title("Europe map")
screen.addshape(IMAGE)
Turtle(shape=IMAGE)

# country_list = pd.DataFrame()

def get_mouse_click_coord(x, y):
    country = screen.textinput("Enter the name of the country.", "Country: ")
    print(x, y)
    country = {
        "country": [country],
        "x_coord": [x],
        "y_coord": [y],
    }
    country_df = pd.DataFrame(country)
    country_df.to_csv("european_countries.csv", mode="a", index=False, header=False)

    # screen.exitonclick()

screen.onscreenclick(get_mouse_click_coord)
screen.mainloop()

# screen.exitonclick()

