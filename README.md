# Customer Churn Prediction (End-to-End MLOps Project)

## Project Overview

This project predicts whether a customer will churn (leave) or not using machine learning.

## Problem Statement

Customer churn prediction helps businesses retain customers and reduce revenue loss.

## Tech Stack

* Python
* Scikit-learn
* Flask (API)
* Docker
* GitHub Actions (CI/CD)
* Render (Deployment)

## ML Pipeline

1. Data Cleaning
2. Feature Engineering
3. Model Training (Multiple Models)
4. Best Model Selection
5. API Development
6. Dockerization
7. CI/CD Pipeline
8. Cloud Deployment

## Best Model

Logistic Regression
Accuracy: ~81%

## Live API

👉 https://your-render-url.onrender.com

## API Usage

POST `/predict`

Example:

```json
{
  "tenure": 12,
  "MonthlyCharges": 50
}
```

Response:

```json
{
  "prediction": 0
}
```

## Project Structure

* app/ → API + model
* src/ → training code
* notebooks/ → preprocessing & feature engineering
* data/ → dataset (ignored)

## Future Improvements

* Add frontend UI
* Model tuning
* Monitoring (Grafana/Prometheus)

---

⭐ If you like this project, give it a star!
