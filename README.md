# 🏠 House Price Prediction - Amsterdam Market Intelligence

A premium web application that provides real-time house price estimations for the Amsterdam real estate market. Powered by XGBoost and wrapped in a modern, glassmorphism-inspired Flask interface.

![Modern UI](https://img.shields.io/badge/UI-Modern_Glassmorphism-blueviolet)
![Engine](https://img.shields.io/badge/Engine-XGBoost_3.2.0-orange)
![Framework](https://img.shields.io/badge/Framework-Flask_3.1.3-green)

---

## ✨ Key Features

- **🚀 Real-time Predictions**: Instant market value estimations using a trained XGBoost model.
- **🎨 Premium UI**: Beautiful, responsive interface with a glassmorphism design system.
- **⚡ AJAX Integration**: Smooth, non-reloading form submissions for a seamless user experience.
- **📊 Robust Preprocessing**: Sophisticated backend handling of features like Area, Rooms, Longitude, and Latitude.

---

## 🛠️ Tech Stack

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
- **Machine Learning**: [XGBoost](https://xgboost.readthedocs.io/), [Pandas](https://pandas.pydata.org/), [Scikit-learn](https://scikit-learn.org/)
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), JavaScript (ES6+)
- **Storage**: Joblib for serialized model and column metadata.

---

## 📂 Project Structure

```text
House-price-prediction/
├── web/
│   ├── static/           # CSS and Assets
│   ├── templates/        # HTML Templates
│   └── app.py            # Flask Backend Logic
├── housepricepred.pkl    # Trained XGBoost Model
├── columns.pkl           # Feature Metadata
├── requirements.txt      # Dependency List
├── HousePriceTrain.ipynb # Training Workflow
└── README.md             # Project Documentation
```

---

## 🚀 Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd House-price-prediction
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/Scripts/activate  # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirement.txt
   ```

4. **Run the Application**:
   ```bash
   python web/app.py
   ```
   *Access the app at `http://127.0.0.1:5000`*

---

## 🧪 Model Details

The estimation engine uses an **XGBoost Regressor** trained on historical Amsterdam housing data. 
- **Target Variable**: Log-transformed Price (for better handling of variance).
- **Features**: Address, Zip Code (encoded), Area (m²), Room count, Longitude, and Latitude.
- **Version**: Trained on XGBoost 3.2.0 for optimal performance and feature scaling.

---

## 📝 License

&copy; 2026 Amsterdam Real Estate Predictor.
