# error chekcing for the format of the inputs, make sure theyre either floats or int
# add the save and load model bonus point
# weite readmee file


from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump, load

app = Flask(__name__)

df = None
model = None
X_train, X_test, y_train, y_test = None, None, None, None

@app.route('/')
def index():
    return render_template('index7.html')

@app.route('/upload', methods=['POST'])
def upload():
    global df, model, X_train, X_test, y_train, y_test

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)

        selected_fields = ['bed', 'bath', 'house_size', 'acre_lot', 'zip_code']
        target_field = 'price'
        X = df[selected_fields]
        y = df[target_field]

        # Split dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestRegressor()
        model.fit(X_train, y_train)

        return jsonify({"message": "Model training is completed!"}), 200
    else:
        return jsonify({"error": "Invalid file format, please upload a CSV file"}), 400




@app.route('/predict', methods=['POST'])
def predict():
    if df is None or model is None:
        return jsonify({"error": "Model is not trained yet"}), 400

    input_data = request.get_json()

    prediction_fields = ['bed', 'bath', 'house_size', 'acre_lot', 'zip_code']
    input_features = [input_data[field] for field in prediction_fields]

    predicted_price = model.predict([input_features])
    return jsonify({"predicted_price": predicted_price[0]})

@app.route('/accuracy')
def accuracy():
    if model is None or X_test is None or y_test is None:
        return jsonify({"error": "Model or test data is not available"}), 400

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    accuracy = 1 - (mse / y_test.var())

    return jsonify({"accuracy": accuracy})

if __name__ == '__main__':
    app.run(debug=True)

