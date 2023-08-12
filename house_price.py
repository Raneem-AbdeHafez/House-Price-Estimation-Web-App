# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Train the model
def train_model(data):
    X = data.drop('price', axis=1)
    y = data['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

# Predict house price
def predict_price(model, bed, bath, house_size, acre_lot, zip_code):
    data = [[zip_code, bed, bath, house_size, acre_lot]]
    prediction = model.predict(data)
    return prediction[0]

# Main function to run the Flask web application
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    data = load_data(file)
    model = train_model(data)
    return "Model trained successfully!"

@app.route('/predict', methods=['POST'])
def predict():
    zip_code = int(request.form['zip_code'])
    house_size = float(request.form['house_size'])
    acre_lot = float(request.form['acre_lot'])
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])
    
    prediction = predict_price(model, bed, bath, house_size, acre_lot, zip_code)
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(debug=True)
