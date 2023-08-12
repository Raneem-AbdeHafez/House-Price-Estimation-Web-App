"""
import pandas as pd
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

app = Flask(__name__)
def train_model(csv_file):
    # Load the CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file)

    # Separate the features (X) and target variable (y)
    X = data.drop("price", axis=1)
    y = data["price"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForestRegressor model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(model, "house_price_model.joblib")

    return model

@app.route("/", methods=["GET", "POST"])
def index():
    csv_file = "data.csv"  # Replace with the actual path to your CSV file

    if request.method == "POST":
        # User input for prediction
        zip_code = int(request.form["zip_code"])
        square_meters = float(request.form["square_meters"])
        acre_size = float(request.form["acre_size"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])

        # Load the trained model or train a new one if it doesn't exist
        try:
            model = joblib.load("house_price_model.joblib")
        except FileNotFoundError:
            model = train_model(csv_file)

        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            "Zip Code": [zip_code],
            "Square Meters": [square_meters],
            "Acre Size": [acre_size],
            "Bedrooms": [bedrooms],
            "Bathrooms": [bathrooms]
        })

        # Use the model to predict the price
        predicted_price = model.predict(input_data)[0]

        return render_template("index.html", predicted_price=predicted_price)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
"""

"""
import os
import pandas as pd
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def train_model(csv_file):
    # Load the CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file)

    # Separate the features (X) and target variable (y)
    X = data.drop("price", axis=1)
    y = data["price"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForestRegressor model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(model, "house_price_model.joblib")

    return model

@app.route("/", methods=["GET", "POST"])
def index():
    csv_file = "data.csv"  # Replace with the actual path to your CSV file

    if request.method == "POST":
        if "file" in request.files:
            uploaded_file = request.files["file"]
            if uploaded_file.filename != "":
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
                uploaded_file.save(file_path)
                csv_file = file_path

        # User input for prediction
        zip_code = int(request.form["zip_code"])
        square_meters = float(request.form["square_meters"])
        acre_size = float(request.form["acre_size"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])

        # Load the trained model or train a new one if it doesn't exist
        try:
            model = joblib.load("house_price_model.joblib")
        except FileNotFoundError:
            model = train_model(csv_file)

        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            "Zip Code": [zip_code],
            "Square Meters": [square_meters],
            "Acre Size": [acre_size],
            "Bedrooms": [bedrooms],
            "Bathrooms": [bathrooms]
        })

        # Use the model to predict the price
        predicted_price = model.predict(input_data)[0]

        return render_template("index.html", predicted_price=predicted_price)

    return render_template("index.html")

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True)
"""