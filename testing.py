import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index5.html')

@app.route('/train', methods=['POST'])
def train():
    file = request.files['csvFile']
    selected_fields = request.form.getlist('field')

    if not file:
        return {'error': 'No CSV file uploaded'}

    data = pd.read_csv(file)
    X = data[selected_fields]
    y = data['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return {'message': 'Model trained successfully'}

@app.route('/predict', methods=['POST'])
def predict():
    zip_code = int(request.form.get('zip_code'))
    square_meters = float(request.form.get('house_size'))
    acre_size = float(request.form.get('acre_lot'))
    bedrooms = int(request.form.get('bed'))
    bathrooms = int(request.form.get('bath'))

    input_data = np.array([[zip_code, square_meters, acre_size, bedrooms, bathrooms]])
    
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    prediction = model.predict(input_data)[0]
    return {'predicted_price': prediction}

if __name__ == "__main__":
    app.run(debug=True)
