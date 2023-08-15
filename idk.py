from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

app = Flask(__name__)

# Global variables
model = None
selected_features = []

def train_model(data, target):
    global model
    model = LinearRegression()
    model.fit(data, target)

def calculate_model_accuracy(data, target):
    global model
    predictions = model.predict(data)
    accuracy = r2_score(target, predictions)
    return accuracy

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/upload', methods=['POST'])
def upload_csv():
    global selected_features
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        df = pd.read_csv(file)
        selected_features = df.columns.tolist()
        return jsonify({"selected_features": selected_features})
    
    return jsonify({"error": "File upload failed"}), 500

@app.route('/train', methods=['POST'])
def train():
    global model, selected_features
    if not model:
        return jsonify({"error": "Model not initialized"}), 400
    
    data = pd.read_csv(request.json['data'])
    target = data.pop('price')  # Assuming 'price' is the target column name
    data = data[selected_features]  # Select only the chosen features
    
    train_model(data, target)
    accuracy = calculate_model_accuracy(data, target)
    return jsonify({"message": "Model trained successfully", "accuracy": accuracy})

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "Model not initialized"}), 400
    
    input_data = request.json['input_data']
    prediction = model.predict([input_data])[0]
    return jsonify({"predicted_price": prediction})

if __name__ == '__main__':
    app.run(debug=True)
