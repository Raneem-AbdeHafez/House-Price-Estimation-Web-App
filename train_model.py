from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor

data= pd.read_csv('house_zipcode_usa.csv')
 
X = data.drop(['price'], axis=1)
Y = data['price']
 
# Split the training set into
# training and validation set
X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, train_size=0.8, test_size=0.2, random_state=0)

 
model_RFR = RandomForestRegressor(n_estimators=10)
model_RFR.fit(X_train, Y_train)
Y_pred = model_RFR.predict(X_valid)
 
print(mean_absolute_percentage_error(Y_valid, Y_pred))

import numpy as np

def predict_single_price(zip_code, house_size, acre_lot, bedrooms, bathrooms):
    # Create a numpy array with the input features in the same order as during training
    input_features = np.array([[zip_code, house_size, acre_lot, bedrooms, bathrooms]])

    # Predict the price using the trained model
    predicted_price = model_RFR.predict(input_features)[0]
    return predicted_price


while True:
# Example input values
    zip_code = int(input("zipcode: "))
    house_size = float(input("house size: "))
    acre_lot = float(input("arce lot: "))
    bedrooms = int(input("beds: "))
    bathrooms = int(input("baths: "))

    # Get the predicted price using the function
    predicted_price = predict_single_price(zip_code, house_size, acre_lot, bedrooms, bathrooms)
    print(f"Predicted Price: ${predicted_price:.2f}")



"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train_model():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file selected'})

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)
        
        # Preprocess the data and split into features and labels
        X = df[['zip_code', 'house_size', 'acre_lot', 'bed', 'bath']]
        y = df['price']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # Feature scaling using StandardScaler
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Train the Linear Regression model
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)

        # Save the trained model and scaler to disk
        joblib.dump(model, 'trained_model.joblib')
        joblib.dump(scaler, 'scaler.joblib')

        # Calculate the R-squared score on the test set
        r_squared = model.score(X_test_scaled, y_test)
        print(f'\nR-squared on test set: {r_squared}\n')

        return jsonify({'message': 'Model trained successfully'})

@app.route('/predict', methods=['POST'])
def predict_price():
    if request.method == 'POST':
        data = request.get_json()

        # Load the trained model and scaler
        model = joblib.load('trained_model.joblib')
        scaler = joblib.load('scaler.joblib')

        # Preprocess the user input
        zip_code = data['zip_code']
        house_size = data['house_size']
        acre_lot = data['acre_lot']
        bedrooms = data['bedrooms']
        bathrooms = data['bathrooms']

        # Feature scaling using the same scaler used during training
        input_features = [[zip_code, house_size, acre_lot, bedrooms, bathrooms]]
        input_features_scaled = scaler.transform(input_features)

        # Predict the price
        predicted_price = model.predict(input_features_scaled)[0]

        return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)








"""