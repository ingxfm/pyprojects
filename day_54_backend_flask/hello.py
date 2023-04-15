from flask import Flask


def make_bold(function):
    def wrapper_bold():
        return f'<b>{function()}</b>'
    return wrapper_bold


def make_emphasis(function):
    def wrapper_emphasis():
        return f'<em>{function()}</em>'
    return wrapper_emphasis


def make_underlined(function):
    def wrapper_underlined():
        return f'<u>{function()}</u>'
    return wrapper_underlined


app = Flask(__name__)

print(__name__)


# different routes using app.route decorator
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://giphy.com/embed/ZFFVNwIbjsKtP3lHYK" width=200 alt="dog-image">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


# creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name}, you are {number} years old.'


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    # add or not: debug=True inside the parentheses
    app.run(debug=True)
