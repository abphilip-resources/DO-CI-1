from flask import Flask, render_template, flash
from flask import request, jsonify, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1> Allen's App using Flask <h1>"

@app.route('/alerts/create')
def create():
    try: return jsonify({'message':'Alert created successfully'})
    except: return jsonify({'message':'Error creating alert'})

@app.route('/alerts/delete')
def delete():
    try: return jsonify({'message':'Alert deleted successfully'})
    except: return jsonify({'message':'Error deleting alert'})

if __name__ == "__main__":
    app.run(debug=True)