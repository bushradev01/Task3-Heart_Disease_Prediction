🫀 Heart Disease Prediction Using Machine Learning (Task 3)
1. Project Title

Heart Disease Prediction Using Machine Learning

2. Objective

To build a machine learning model that predicts whether a person is at risk of heart disease based on medical parameters.

3. Dataset
Dataset: Heart Disease UCI Dataset https://www.kaggle.com/datasets/navjotkaushal/heart-disease-uci-dataset/data
Source: Kaggle
Size: 918 records, 12 features
Target Variable:
0 → No heart disease
1 → Heart disease present
5. Data Preprocessing

The following preprocessing steps were applied:

Converted categorical variables:
Sex → Male/Female → 0/1
Chest Pain Type → One-hot encoding
Resting ECG → One-hot encoding
Converted boolean values:
True/False → 0/1
Ensured all features were numeric for ML models
Applied StandardScaler for feature scaling
5. Exploratory Data Analysis (EDA)

Key insights:

Target distribution: balanced dataset (508 vs 410)
Important correlations:
exang → positive correlation with heart disease
oldpeak → strong indicator
thalch → negative correlation
Most important features:
Chest pain type
Oldpeak
Max heart rate
6. Model Training

Models used:

Logistic Regression
Decision Tree
Random Forest

Training process:

Train-test split: 80/20
Feature scaling using StandardScaler
Model training and evaluation
7. Model Evaluation
Model	Accuracy
Logistic Regression	80.43%
Decision Tree	78.80%
Random Forest	82.60%

✔ Confusion Matrix used for evaluation
✔ ROC-AUC Score ≈ 0.91

8. Final Model Selection

✔ Final Model: Logistic Regression

Why Logistic Regression?

Although Random Forest achieved the highest accuracy (~82.6%), the project requirement allowed only Logistic Regression for final deployment.

✔ Stable and interpretable model
✔ Good balance of precision and recall
✔ Accuracy: 80.43%

9. Deployment (Streamlit App)

✔ Saved files:

model.pkl
scaler.pkl
App Functionality:
User enters medical parameters
Model predicts heart disease risk
Output:
🚨 High Risk of Heart Disease
✅ No Heart Disease Risk
10. Conclusion
Machine learning can effectively predict heart disease risk
Random Forest performed best in experiments (~82.6%)
Final deployed model: Logistic Regression (~80.43%)
Key predictors:
Chest pain type
Oldpeak
Maximum heart rate
