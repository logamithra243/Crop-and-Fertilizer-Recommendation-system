from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import pandas as pd
import re
from crop_rec import crecommend
from f_rec import frecommend
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key
client = MongoClient('localhost', 27017)
db = client['your_database_name']  # Replace with your MongoDB database name
users_collection = db['users']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def layout():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        if users_collection.find_one({'username': username}):
            flash('Username already exists. Choose a different one.', 'danger')
        else:
            users_collection.insert_one({'username': username, 'password': password})
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            flash('Login successful.', 'success')
            return redirect(url_for('layout'))
            # Add any additional logic, such as session management
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')
 


@app.route('/crop_recommendation', methods=['GET', 'POST'])
def crop_recommendation():
    title = 'Crop Recommendation'
    acc=None
    if request.method == 'POST':
        Nitrogen=float(request.form['nitrogen'])
        Phosphorus=float(request.form['phosphorus'])
        Potassium=float(request.form['potassium'])
        Temperature=float(request.form['temperature'])
        Humidity=float(request.form['humidity'])
        Ph=float(request.form['ph'])
        Rainfall=float(request.form['rainfall'])
        values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
        input = pd.DataFrame({
            'N': [Nitrogen],
            'P': [Phosphorus],
            'K': [Potassium],
            'temperature': [Temperature],
            'humidity': [Humidity],
            'ph': [Ph],
            'rainfall': [Rainfall]
        })
        acc=crecommend(input)
        
        
    return render_template('crop_recommendation.html', prediction=str(acc),title=title)


    
@app.route('/fertilizer_recommendation', methods=['GET', 'POST'])
def fertilizer_recommendation_route():
    title = 'Fertilizer recommendation'
    acc = None
    if request.method == 'POST':
        # Retrieve form data
        Temparature = float(request.form['temperature'])
        Humidity = float(request.form['humidity'])
        Moisture = float(request.form['moisture'])
        Nitrogen = float(request.form['nitrogen'])
        Phosphorous = float(request.form['phosphorus'])
        Potassium = float(request.form['potassium'])
        Soil_Num = request.form['soilType']
        Crop_Num = request.form['cropType']

        # Call your recommendation function
        acc = frecommend(Temparature,Humidity,Moisture,Nitrogen,Potassium,Phosphorous,Soil_Num,Crop_Num)

    return render_template('fertilizer_recommendation.html', prediction=str(acc), title=title)
    

    
if __name__ == '__main__':
    app.run(debug=True)