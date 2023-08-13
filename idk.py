from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["csv_file"]
        if uploaded_file.filename != "":
            data = pd.read_csv(uploaded_file)
            app.feature_columns = data.columns.tolist()  # Save feature column names
            X = data.drop(['price'], axis=1)
            Y = data['price']
            X_train, _, Y_train, _ = train_test_split(X, Y, train_size=0.8, random_state=0)
            model_RFR = RandomForestRegressor(n_estimators=10)
            model_RFR.fit(X_train, Y_train)

            app.model_RFR = model_RFR

            return render_template("index1.html", message="Model trained successfully!")

    return render_template("index1.html", message="Upload a CSV file to train the model.")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    print("Received data:", data)
    zip_code = int(data["zip_code"])
    house_size = float(data["house_size"])
    acre_lot = float(data["acre_lot"])
    bedrooms = int(data["bedrooms"])
    bathrooms = int(data["bathrooms"])

    model_RFR = app.model_RFR
    feature_columns = app.feature_columns  # Get the feature column names
    input_features = [zip_code, house_size, acre_lot, bedrooms, bathrooms]
    input_features_dict = {col: value for col, value in zip(feature_columns, input_features)}

    input_features_df = pd.DataFrame([input_features_dict])  # Create a DataFrame with feature names
    predicted_price = model_RFR.predict(input_features_df)[0]

    return jsonify({"predicted_price": predicted_price})


if __name__ == "__main__":
    app.run(debug=True)
