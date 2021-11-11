from flask import Flask

app = Flask(__name__)                       # App created

@app.route('/')                             # Decorator for showing the home page path
def a():
    return '<h1>Fibonacci</h1>'             # Return the html code

@app.route('/allen')                        # Decorator for showing the allen page path
def b():
    return '<b>1, 1, 2, 3, 5, 8... </b>'    # Return the html code