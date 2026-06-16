# 📊 HR Analytics - Employee Attrition Prediction

## Overview

This project predicts whether an employee is likely to leave the company using Machine Learning techniques. The objective is to help HR departments identify employees at risk of attrition and take proactive retention measures.

The project includes data preprocessing, exploratory data analysis (EDA), feature importance analysis, model training, and an interactive Streamlit dashboard for real-time predictions.

---

## Problem Statement

Employee attrition can significantly impact organizational productivity and costs. This project aims to analyze employee-related factors and predict attrition using historical HR data.

---

## Dataset

**Dataset:** IBM HR Analytics Employee Attrition Dataset

The dataset contains employee information such as:

* Age
* Monthly Income
* Distance From Home
* OverTime Status
* Total Working Years
* Years At Company
* Job Satisfaction
* Education
* Department
* and other HR-related attributes

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit

---

## Machine Learning Model

**Algorithm Used:** Random Forest Classifier

Random Forest was selected because it:

* Handles tabular data effectively
* Reduces overfitting
* Provides feature importance analysis
* Delivers strong predictive performance

---

## Model Performance

* Model Accuracy: **86%**
* Evaluation Metrics:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report

---

## Key Factors Influencing Attrition

Feature importance analysis identified the following important factors:

1. Monthly Income
2. OverTime
3. Age
4. Distance From Home
5. Total Working Years
6. Years At Company

---

## Streamlit Dashboard Features

* Interactive employee attrition prediction
* User-friendly input form
* Probability-based predictions
* Real-time prediction results
* HR Analytics dashboard interface

---

## Project Structure

HR_attrition_prediction/

├── app.py

├── attrition_dashboard_model.pkl

├── WA_Fn-UseC_-HR-Employee-Attrition.csv

├── HR_Attrition_Prediction.ipynb

├── screenshots/

└── README.md

---

## How to Run the Project

### Clone the Repository

```bash
git clone <repository-link>
```

### Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

### Run the Dashboard

```bash
streamlit run app.py
```

---

## Future Improvements

* Deploy dashboard on Streamlit Cloud
* Add more visual analytics
* Improve model performance with hyperparameter tuning
* Add multiple machine learning model comparisons

---

## Author

**Janvi Gogeri**

B.Tech (Artificial Intelligence Specialization)

