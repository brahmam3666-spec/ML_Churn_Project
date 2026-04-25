from flask import Flask, request, jsonify, Response
import joblib
import pandas as pd
from prometheus_client import Counter, generate_latest
import os

app = Flask(__name__)

# Metric
REQUEST_COUNT = Counter('request_count', 'Total API Requests')

# Load model (ONLY ONCE)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
columns = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))

@app.route('/')
def home():
    return "Churn Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    REQUEST_COUNT.inc()

    data = request.json
    df = pd.DataFrame([data])
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return jsonify({"prediction": int(prediction)})

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)