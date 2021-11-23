# https://realpython.com/api-integration-in-python/

from flask import Flask, render_template, flash
from flask import request, jsonify, redirect

app = Flask(__name__)                                                   # App created

@app.route('/')                                                         # Decorator for showing the home page path
def home():
    return '<h1>Allen</h1>'                                             # Return the html code

@app.route('/a')                                                        # Decorator for showing the 'a' page path
def a():
    return '''<h1>Allen</h1><br/>
    <h2>Contact me</h2>
    <b>9449277201, allenbphilip@gmail.com</b>'''                        # Return the html code

@app.route('/b')                                                        # Decorator for showing the 'b' page path
def b():
    return '''<h1>Allen</h1><br/>
    <h2>Occupation</h2>
    <i>Data Analyst at ZS</i>'''                                        # Return the html code

@app.route('/c')                                                        # Decorator for showing the 'c' page path
def c():
    return '''<h1>Allen</h1><br/>
    <h2>Website</h2>
    <a href="https://abphilip.me">Click Here</b>'''                     # Return the html code

@app.route('/alerts/create')                                            # Create page path
def create():
    try: return jsonify({'message':'Alert created successfully'})       
    except: return jsonify({'message':'Error creating alert'})          

@app.route('/alerts/delete')                                            # Delete page path
def delete():
    try: return jsonify({'message':'Alert deleted successfully'})
    except: return jsonify({'message':'Error deleting alert'})

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}    
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

'''
    curl -i http://127.0.0.1:5000/countries \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{"name":"Germany", "capital": "Berlin", "area": 357022}'
'''

if __name__ == "__main__":
    app.run(debug=True)