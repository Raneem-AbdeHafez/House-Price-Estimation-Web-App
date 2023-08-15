import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class HousePriceEstimationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("House Price Estimation")
        
        self.model = None
        self.selected_features = []
        self.file_path = None
        
        self.create_widgets()
        
    def create_widgets(self):
        self.upload_button = tk.Button(self.root, text="Upload CSV File", command=self.upload_csv)
        self.upload_button.pack()
        
        self.features_label = tk.Label(self.root, text="Select Features:")
        self.features_label.pack()
        self.feature_checkboxes = []
        
        self.train_button = tk.Button(self.root, text="Train Model", state=tk.DISABLED, command=self.train)
        self.train_button.pack()
        
        self.zip_code_entry = tk.Entry(self.root, width=30)
        self.zip_code_entry.pack()
        self.square_meters_entry = tk.Entry(self.root, width=30)
        self.square_meters_entry.pack()
        self.acre_size_entry = tk.Entry(self.root, width=30)
        self.acre_size_entry.pack()
        self.bedrooms_entry = tk.Entry(self.root, width=30)
        self.bedrooms_entry.pack()
        self.bathrooms_entry = tk.Entry(self.root, width=30)
        self.bathrooms_entry.pack()
        
        self.predict_button = tk.Button(self.root, text="Predict Price", state=tk.DISABLED, command=self.predict)
        self.predict_button.pack()
        
        self.predicted_price_label = tk.Label(self.root, text="Predicted Price:")
        self.predicted_price_label.pack()
        
    def upload_csv(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.file_path:
            df = pd.read_csv(self.file_path, index_col=None)  # Specify index_col=None
            print("Loaded DataFrame columns:", df.columns)
            self.selected_features = df.columns.tolist()
            self.update_feature_checkboxes()
            self.train_button.config(state=tk.NORMAL)

    
    def update_feature_checkboxes(self):
        for checkbox in self.feature_checkboxes:
            checkbox.destroy()
        self.feature_checkboxes = []
        
        for feature in self.selected_features:
            checkbox = tk.Checkbutton(self.root, text=feature)
            checkbox.pack()
            self.feature_checkboxes.append(checkbox)
    
    def train(self):
        if self.selected_features and self.file_path:
            self.model = RandomForestRegressor()
            data = pd.read_csv(self.file_path)
            
            print("Loaded DataFrame columns:", data.columns)
            
            if 'price' in data.columns:
                target = data['price']
                data = data.drop(columns=['price'])
                self.model.fit(data, target)
                self.predict_button.config(state=tk.NORMAL)
            else:
                print("Error: 'price' column not found.")


    
    def predict(self):
        if self.model:
            input_data = {
                'zipCode': self.zip_code_entry.get(),
                'squareMeters': float(self.square_meters_entry.get()),
                'acreSize': float(self.acre_size_entry.get()),
                'bedrooms': int(self.bedrooms_entry.get()),
                'bathrooms': int(self.bathrooms_entry.get())
            }
            prediction = self.model.predict([list(input_data.values())])[0]
            self.predicted_price_label.config(text=f"Predicted Price: ${prediction:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HousePriceEstimationApp(root)
    root.mainloop()
