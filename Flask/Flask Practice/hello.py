import re
from flask import Flask,render_template
import random
from datetime import date
import requests
from blog_posts import blogs

app = Flask(__name__)

@app.route("/")
def index():
    random_number = random.randint(1,20)
    current_year = date.today().year
    return render_template('index.html',rand_num = random_number,year=current_year)

@app.route('/guess/<name>')
def guess(name):
    generize_url = f'https://api.genderize.io?name={ name }'
    data = requests.get(generize_url)
    json_form_data = data.json()
    gender = json_form_data['gender']

    agify_url = f'https://api.agify.io?name={name}'
    data = requests.get(agify_url)
    json_data = data.json()
    age = json_data['age']
    return render_template('guess.html',person_name=name,gender=gender,age=age)


@app.route('/blog')
def blog_page():
   return render_template('blog.html',posts=blogs)


@app.route('/username/<name>/<int:number>')
def greet(name,number):
    return f'Hello {name} ,you are {number} old.'


if __name__ == "__main__":
    app.run(debug=True)