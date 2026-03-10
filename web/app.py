import os
import joblib
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base path relative to app.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the model and columns
def load_assets():
    model_path = os.path.join(BASE_DIR, 'housepricepred.pkl')
    columns_path = os.path.join(BASE_DIR, 'columns.pkl')
    
    # Using joblib as seen in training code
    model = joblib.load(model_path)
    columns = joblib.load(columns_path)
    return model, columns

model, model_columns = load_assets()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        address = request.form.get('address', '')
        zip_code = request.form.get('zip', '')
        area = float(request.form.get('area', 0))
        rooms = int(request.form.get('rooms', 0))
        lon = float(request.form.get('lon', 0))
        lat = float(request.form.get('lat', 0))

        # 1. Create initial DataFrame with features matching raw data structure
        # (excluding Price)
        raw_data = {
            'Address': address,
            'Zip': zip_code,
            'Area': area,
            'Room': rooms, # Training data uses 'Room' (singular)
            'Lon': lon,
            'Lat': lat
        }
        df = pd.DataFrame([raw_data])
        
        
        # We need to create the exact columns the model saw
        X = pd.get_dummies(df)
        
        # Align with model_columns
        X = X.reindex(columns=model_columns, fill_value=0)
        
        # 3. Make Prediction
        # Model was trained on log1p(Price)
        log_prediction = model.predict(X)
        
        # 4. Inverse Transformation
        final_prediction = np.expm1(log_prediction)[0]
        
        return jsonify({
            'success': True,
            'prediction': f"€ {final_prediction:,.2f}"
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)