from flask import Flask
from random import randint


random_number = randint(0, 101)
print(random_number)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 100</h1>' \
           '<br>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<number>')
def compare_number(number):
    try:
        if int(number) == random_number:
            return '<h1 style="color: green">You found me!</h1>' \
                   '<br>' \
                   '<img src="https://media.giphy.com/media/woyu4rzNJ3AYg/giphy.gif">'

        elif int(number) < random_number:
            return '<h1 style="color: red">Too low</h1>' \
                   '<br>' \
                   '<img src="https://media.giphy.com/media/12bpEjD05ac2IM/giphy.gif">'

        else:
            return '<h1 style="color: blue">Too high</h1>' \
                   '<br>' \
                   '<img src="https://media.giphy.com/media/yXBqba0Zx8S4/giphy.gif">'
    except TypeError as TE:
        print(TE)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
