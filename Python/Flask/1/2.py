from flask import Flask, render_template, request, flash, jsonify, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return "Allen's App using Flask"

@app.route('/alerts/create')
def create():
    try:
        return jsonify({'message':'Alert created successfully'})
    except: return jsonify({'message':'Error creating alert'})

@app.route('/alerts/delete')
def delete():
    try:
        return jsonify({'message':'Alert deleted successfully'})
    except: return jsonify({'message':'Error deleting alert'})

if __name__ == "__main__":
    app.run(debug=True)