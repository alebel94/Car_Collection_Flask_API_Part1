from car_collection_api import app 
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')