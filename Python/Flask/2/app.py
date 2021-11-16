import json                                                                     # JSON handling
import os.path                                                                  # File handling
from werkzeug.utils import secure_filename                                      # Ensuring security of uploaded file 
from flask import Flask                                                         # Web app construction
from flask import request                                                       # Handling user I/O
from flask import redirect                                                      # URL Redirection
from flask import render_template                                               # Return a webpage
from flask import url_for                                                       # Return the URL for an object
from flask import flash                                                         # Alert messages
from flask import abort                                                         # Abort a request
from flask import session                                                       # Session handling for user
from flask import jsonify                                                       # Converting to JSON

app = Flask(__name__)                                                           # Name of the app
app.secret_key = 'Alvin333#'                                                    # Secret Key

@app.route('/')                                                                 # Home Page
def home():
    return render_template('home.html', codes=session.keys())                   # Display home.html

@app.route('/your-url', methods=['GET','POST'])                                 # GET & POST methods accepted
def your_url():
    if(request.method=='GET'): return redirect(url_for('home'))                 # If GET, redirect to home page
    else:
        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            flash('''That short name has already been taken. 
                    Please select another name.''')
            return redirect(url_for('home'))

        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/Users/allen/OneDrive/Desktop/Github/Learning/Python/Flask/2/static/files' 
                    + full_name)
            urls[request.form['code']] = {'file':full_name}


        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
            session[request.form['code']] = True
        return render_template('your_url.html', code=request.form['code'])

@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static', 
                    filename='files/'+ urls[code]['file']))
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/api')
def session_api():
    return jsonify(list(session.keys()))