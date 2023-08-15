# works perfectly along side index3

from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

model = None
selected_features = []

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
        model = LinearRegression()
    
    data = pd.read_csv(request.json['data'])
    target = data.pop('price')  # Assuming 'price' is the target column name
    data = data[selected_features]  # Select only the chosen features
    
    model.fit(data, target)
    return jsonify({"message": "Model trained successfully"})

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if not model:
        return jsonify({"error": "Model not trained"}), 400
    
    input_data = request.json['input_data']
    prediction = model.predict([input_data])[0]
    return jsonify({"predicted_price": prediction})

if __name__ == '__main__':
    app.run(debug=True)
