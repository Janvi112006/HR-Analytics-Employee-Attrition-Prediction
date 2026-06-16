import streamlit as st
import pickle
import pandas as pd

# Load model
with open("attrition_dashboard_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("📊 HR Analytics Dashboard")

st.markdown("### Employee Attrition Prediction")

st.write("""
This dashboard predicts whether an employee is likely to leave the company
based on important HR factors.
""")

st.sidebar.info(
    "This project predicts employee attrition using Machine Learning."
)

st.metric("Model Accuracy", "86%")

age = st.slider("Age", 18, 60, 30)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=1000,
    max_value=50000,
    value=10000
)

overtime = st.selectbox(
    "OverTime",
    ["No", "Yes"]
)

distance = st.slider(
    "Distance From Home",
    1,
    30,
    5
)

total_working_years = st.slider(
    "Total Working Years",
    0,
    40,
    5
)

years_company = st.slider(
    "Years At Company",
    0,
    40,
    5
)

overtime = 1 if overtime == "Yes" else 0

if st.button("Predict Attrition"):

    data = pd.DataFrame({
        'Age':[age],
        'MonthlyIncome':[monthly_income],
        'OverTime':[overtime],
        'DistanceFromHome':[distance],
        'TotalWorkingYears':[total_working_years],
        'YearsAtCompany':[years_company]
    })

    prediction = model.predict(data)

    probability = model.predict_proba(data)

    leave_prob = probability[0][1]
    stay_prob = probability[0][0]

    st.write(f"Stay Probability: {stay_prob:.2%}")
    st.write(f"Leave Probability: {leave_prob:.2%}")

    if prediction[0] == 1:
        st.error("⚠️ Employee likely to leave")
    else:
        st.success("✅ Employee likely to stay")
st.markdown("---")
st.write("Developed by Janvi Gogeri")