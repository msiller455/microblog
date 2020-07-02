from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    posts = [
        {
            'author': {'username': 'Joe'},
            'body': 'Blahblahblah'
        },
        {
            'author': {'username': 'Boe'},
            'body': 'Yoyoyoyo'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)