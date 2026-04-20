import streamlit as st
import requests

st.title("Customer Churn Prediction")

# Inputs
tenure = st.number_input("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0, 200, 50)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

if st.button("Predict"):

    data = {
        "tenure": tenure,
        "MonthlyCharges": monthly,

        "Contract_One year": 1 if contract == "One year" else 0,
        "Contract_Two year": 1 if contract == "Two year" else 0,

        "InternetService_Fiber optic": 1 if internet == "Fiber optic" else 0,
        "InternetService_No": 1 if internet == "No" else 0
    }

    try:
        with st.spinner("Predicting... please wait ⏳"):
            response = requests.post(
                "https://churn-ml-api-0br6.onrender.com/predict",
                json=data,
                timeout=10   #  prevents long wait
            )

        # Debug
        st.write("Response:", response.text)

        if response.status_code == 200:
            result = response.json()

            if result["prediction"] == 1:
                st.error("Customer is likely to churn ")
            else:
                st.success("Customer will stay ")

        elif response.status_code == 503:
            st.warning("Server is waking up... try again ")

        else:
            st.error(f"API Error: {response.status_code}")

    except requests.exceptions.Timeout:
        st.error("Server took too long. Try again ")

    except requests.exceptions.RequestException:
        st.error("Connection error. Check API ")