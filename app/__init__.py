from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    list_posts = [
     {
        "author":"deny",
        "post":"Belajar flask bagian1",
        "date": "20/02/2019"
    },
    {
        "author":"deny",
        "post":"Belajar flask bagian2",
        "date": "20/02/2019"
    },
    {
        "author":"deny",
        "post":"Belajar flask bagian3",
        "date": "20/02/2019"
    }
    ]
    return render_template('index.html', data=list_posts)

@app.route('/pena')
def pena():
    data_post = {
    "author":"deny",
    "post":"Belajar flask bagian1",
    "date": "20/02/2019"
    }
    return render_template("pena.html", data=data_post)

# @app.route('/profile')
# def profile():
# 	return render_template('profile.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", data = username)