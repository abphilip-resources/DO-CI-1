from flask import Flask

app = Flask(__name__)                                   # App created

@app.route('/')                                         # Decorator for showing the home page path
def home():
    return '<h1>Allen</h1>'                             # Return the html code

@app.route('/a')                                        # Decorator for showing the a page path
def a():
    return '''<h1>Allen</h1><br/><br/>                                
    <h2>Contact me</h2>
    <b>9449277201, allenbphilip@gmail.com</b>'''        # Return the html code

@app.route('/b')                                        # Decorator for showing the b page path
def b():
    return '''<h1>Allen</h1><br/><br/>                                
    <h2>Occupation</h2>
    <i>Data Analyst at ZS</i>'''                        # Return the html code

@app.route('/c')                                        # Decorator for showing the c page path
def c():
    return '''<h1>Allen</h1><br/><br/>                                
    <h2>Website</h2>
    <a href="https://abphilip.me">Click Here</b>'''     # Return the html code