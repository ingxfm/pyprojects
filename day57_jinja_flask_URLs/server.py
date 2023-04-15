# Built-in
import random
from datetime import datetime

# 3rd-party
from flask import Flask, render_template
import requests

AGE_URL: str = 'https://api.agify.io/'
GENDER_URL: str = 'https://api.genderize.io'


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 11)
    today = datetime.today().year
    return render_template('index.html', num=random_number, date_year=today)


@app.route('/guess/<name>')
def guess(name):
    age_params: dict = {
        'name': name,
    }

    gender_params: dict = {
        'name': name,
    }
    age_info = requests.get(url=AGE_URL, params=age_params).json()
    gender_info = requests.get(url=GENDER_URL, params=gender_params).json()
    print(age_info)
    print(gender_info)
    return render_template('guess.html',
                           name=name.title(),
                           age=age_info['age'],
                           gender=gender_info['gender'])


if __name__ == '__main__':
    app.run(debug=True)
