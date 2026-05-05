import streamlit as st
import requests

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure (Months)", min_value=0)
monthly = st.number_input("Monthly Charge")
total = st.number_input("Total Charges")

if st.button("Predict"):

    data = {
        "Tenure_in_Months": tenure,
        "Monthly_Charge": monthly,
        "Total_Charges": total
    }

    response = requests.post(
        "https://fastapi-churn-isid.onrender.com/predict",
        json=data
    )
    # st.write("Status", response.status_code)
    # st.write("Response:", response.text)
    
    if response.status_code==200:
       result = response.json()

       st.subheader("Sonuç")

       st.write(f"Prediction: {result['prediction']}")
       st.write(f"Probability: % {result['churn_probability']:.2f}")

       segment = result["segment"]

       if segment == "High Risk":
        st.error(segment)
       elif segment == "Medium":
        st.warning(segment)
       else:
        st.success(segment)
    else:
      st.error("Api calismiyor ve ya yanlis response donuyor")