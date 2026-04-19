from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load model
model = joblib.load("app/model.pkl")
columns = joblib.load("app/columns.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return "Churn Prediction API is running"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    df = pd.DataFrame([data])

    # Align columns
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)