# House Price Estimation Web App

This README provides a detailed guide on how to use the House Price Estimation web application, including prerequisites, installation, deployment, build information, and an overview of how the app works.

## Getting Started

The House Price Estimation web app allows you to upload a CSV file containing housing data to train a machine learning model for predicting house prices. Users can also use the trained model to predict house prices for specific input features.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python (3.6 or higher)
- Flask
- pandas
- scikit-learn (sklearn)
- joblib

You can install the required Python packages using the following command:

```bash
pip install Flask pandas scikit-learn joblib
```

## Installing

1. Clone the repository or download the code files to your local machine.

2. Navigate to the project directory using the command line.

3. Run the following command to start the Flask web application:

```bash
python app.py
```

Open your web browser and visit http://localhost:5000 to access the House Price Estimation web app.

- Remember that the app is set to run on localhost at port 5000 by default. If you encounter any issues or have firewall restrictions, ensure that port 5000 is open and available for use.

## Deployment

The web app is set to run in development mode by default. If you plan to deploy this application in a production environment, it is recommended to configure a production-ready web server.

## Build With

The House Price Estimation web app is built using the following technologies:

- Python: Programming language used for backend development.
- Flask: Micro web framework used to build the web application.
- pandas: Library for data manipulation and analysis.
- scikit-learn: Machine learning library used for model training and prediction.
- joblib: Library for saving and loading Python objects, including machine learning models.

## How the App Works

1. **Upload CSV File and Train Model**:
   - Access the web application through a browser.
   - The main page (`/`) contains a form for uploading a CSV file containing housing data.
   - Choose a CSV file using the "Upload CSV File" input and click the "Upload & Train" button.
   - The uploaded CSV file is read, and relevant features and target values are extracted.
   - The data is split into training and testing sets, and a Random Forest Regressor model is trained on the training data.
   - Once training is complete, a message is displayed indicating the completion of model training.

2. **Predict House Price**:
   - Fill out the form in the "Predict House Price" section with the desired input features: bedrooms, bathrooms, house size, acre lot, and zip code.
   - Click the "Predict Price" button.
   - The input data is sent to the server, and the trained model predicts the house price based on the provided features.
   - The predicted price is displayed on the page.

3. **Calculate Accuracy**:
   - Click the "Calculate Accuracy" button.
   - The model's accuracy is calculated using the Mean Squared Error (MSE) metric on the testing data.
   - The accuracy percentage is displayed on the page.

The HTML template (`index7.html`) contains the necessary form elements for interacting with the web app. JavaScript is used to handle form submissions, communicate with the server, and display results on the page.

Please note that this application is for demonstration purposes and may require additional security measures and optimizations before being used in a production environment.

## Challenges Faced
when developing this application, I faced some difficulties with making my model train based on what the user selectes as feilds when uploading the csv file. In other codes, I got the part where you asked from me to show the feilds that were in the csv file auomattically after the file was uploaded, but my model training due to serever connection error, ``` "POST /train HTTP/1.1" 400``` . I tried to fix it and figure out why the issue was surfacing but i couldnt. So for that reason i made another code where I got the machine learnng model working with real data and give out the precited price and accuracy of the model without the user being able to select the fields. if would like to see the version where it the user is able to select the fields from the csv file and train the model from. You can run the python file that runs along side (`index5.html`) or (`index4.html`), either way the model isnt training (change the HTML in python code).

``` bash
python theOne.py
```

## Credits
This project was developed by the R-AI Company (Raneem Abdel Hafez) and is based on the Flask framework and scikit-learn library.

## License
This project is not licensed :)