import json
import requests
import pandas as pd
import pickle
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    output = None
    if request.method == 'POST':
        try:
            # Get JSON string from form and load it as a Python object
            data_json_str = request.form.get('data')
            data_json = json.loads(data_json_str)  # Convert string to JSON
            
            # Extract the 'data' field
            df = pd.DataFrame(data_json['data'])

            # Load model and make predictions
            with open('model/model.pkl', 'rb') as model_file:
                model = pickle.load(model_file)
            
            predictions = model.predict(df).tolist()
            
            # Format predictions to two decimal places
            output = [f"{pred:.2f}" for pred in predictions]
        except Exception as e:
            return str(e)

    return render_template('index.html', output=output)

@app.route('/predict', methods=['POST'])
def predict():
    data_json = request.get_json()['data']
    df = pd.DataFrame(data_json)

    with open('model/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    predictions = model.predict(df).tolist()
    
    # Format predictions to two decimal places
    output = [f"{pred:.2f}" for pred in predictions]
    
    return jsonify({'prediction': output})


if __name__ == '__main__':
    app.run(debug=True)
