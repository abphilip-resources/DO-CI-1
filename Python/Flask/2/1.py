import json
from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name='Allen')

@app.route('/about')
def about():
    return 'URL Shortener'

@app.route('/your-url', methods=['POST','GET'])
def your_url():
    urls = {}
    if(request.method=='POST'):
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            return redirect(url_for('home'))

        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))