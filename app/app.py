from flask import Flask, request, jsonify
import joblib
import pandas as pd
from prometheus_client import Counter, generate_latest

# Load model
model = joblib.load("app/model.pkl")
columns = joblib.load("app/columns.pkl")

# Metric
REQUEST_COUNT = Counter('request_count', 'Total API Requests')

app = Flask(__name__)

@app.route('/')
def home():
    return "Churn Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    REQUEST_COUNT.inc()   # 👈 COUNT REQUEST

    data = request.json
    df = pd.DataFrame([data])
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return jsonify({"prediction": int(prediction)})

from flask import Response

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)