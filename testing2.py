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

def train_model(csv_file, selected_columns):
    # Load only the selected columns from the CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file, usecols=selected_columns)

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

        # Get the selected columns for training
        selected_columns = request.form.getlist("columns")

        # Train the model with the selected columns
        try:
            model = train_model(csv_file, selected_columns)
        except Exception as e:
            return render_template("index.html", error=str(e))

        # User input for prediction
        zip_code = int(request.form["zip_code"])
        square_meters = float(request.form["square_meters"])
        acre_size = float(request.form["acre_size"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])

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

def train_model(csv_file, selected_fields):
    # Load only the selected columns from the CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file, usecols=selected_fields)

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
    selected_fields = []

    if request.method == "POST":
        if "file" in request.files:
            uploaded_file = request.files["file"]
            if uploaded_file.filename != "":
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
                uploaded_file.save(file_path)
                csv_file = file_path

        # Get the selected fields from the form
        selected_fields = request.form.getlist("fields")

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
            model = train_model(csv_file, selected_fields)

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

        return render_template("index.html", predicted_price=predicted_price, selected_fields=selected_fields)

    return render_template("index.html", selected_fields=selected_fields)

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
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

def train_model(csv_file, selected_fields):
    # Load the CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file, usecols=selected_fields + ["price"])

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
    selected_fields = []

    if request.method == "POST":
        if "file" in request.files:
            uploaded_file = request.files["file"]
            if uploaded_file.filename != "":
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
                uploaded_file.save(file_path)
                csv_file = file_path

        # Get the selected fields from the form
        selected_fields = request.form.getlist("fields")

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
            model = train_model(csv_file, selected_fields)

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

        return render_template("index.html", predicted_price=predicted_price, selected_fields=selected_fields)

    return render_template("index.html", selected_fields=selected_fields)

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True)
"""



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
        X = df[['house_size', 'acre_lot', 'bed', 'bath']]
        y = df['price']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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

        return jsonify({'message': 'Model trained successfully'})

@app.route('/predict', methods=['POST'])
def predict_price():
    if request.method == 'POST':
        data = request.get_json()

        # Load the trained model and scaler
        model = joblib.load('trained_model.joblib')
        scaler = joblib.load('scaler.joblib')

        # Preprocess the user input
        house_size = data['house_size']
        acre_lot = data['acre_lot']
        bedrooms = data['bedrooms']
        bathrooms = data['bathrooms']

        # Feature scaling using the same scaler used during training
        input_features = [[house_size, acre_lot, bedrooms, bathrooms]]
        input_features_scaled = scaler.transform(input_features)

        # Predict the price
        predicted_price = model.predict(input_features_scaled)[0]

        return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)

"""





#####################################################################


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
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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


##############################################################


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
        data = pd.read_csv(file)
        
        # Preprocess the data and split into features and labels
        X = data.drop(['price'], axis=1)
        Y = data['price']

        # Split the data into training and testing sets
        X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, train_size=0.8, test_size=0.2, random_state=0)

        # Train the Linear Regression model
        from sklearn.metrics import mean_absolute_percentage_error
        from sklearn.ensemble import RandomForestRegressor
 
        model_RFR = RandomForestRegressor(n_estimators=10)
        model_RFR.fit(X_train, Y_train)
        Y_pred = model_RFR.predict(X_valid)
        
        print(mean_absolute_percentage_error(Y_valid, Y_pred))

        # Save the trained model and scaler to disk
        joblib.dump(model_RFR, 'trained_model.joblib')
        #joblib.dump(scaler, 'scaler.joblib')

        # Calculate the R-squared score on the test set
        #r_squared = model.score(X_test_scaled, y_test)
        #print(f'\nR-squared on test set: {r_squared}\n')

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
        bedrooms = data['bed']
        bathrooms = data['bath']

        # Feature scaling using the same scaler used during training
        input_features = [[zip_code, house_size, acre_lot, bedrooms, bathrooms]]
        input_features_scaled = scaler.transform(input_features)

        # Predict the price
        predicted_price = model.predict(input_features_scaled)[0]

        return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)




