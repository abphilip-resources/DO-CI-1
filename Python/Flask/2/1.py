from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name='Allen')

@app.route('/about')
def about():
    return 'URL Shortener'

@app.route('/your-url')
def your_url():
    return render_template('your_url.html', code=request.args['code'])