🫀 Heart Disease Prediction Using Machine Learning (Task 3)
📌 Project Overview

This project focuses on predicting the risk of heart disease using Machine Learning techniques. The model analyzes various medical attributes of a patient and predicts whether the patient is likely to have heart disease or not.

The project was developed using the Heart Disease UCI Dataset and multiple machine learning algorithms were tested to identify the best-performing model.

🎯 Objective

The main objective of this project is:

To build a machine learning model capable of predicting heart disease risk
To compare multiple ML algorithms
To deploy the final model using Streamlit for real-time predictions
📂 Dataset Information
Dataset

Heart Disease UCI Dataset

Source

Kaggle

Dataset Size
918 records
12 features
Target Variable
Value	Meaning
0	No Heart Disease
1	Heart Disease Present
⚙️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit
🧹 Data Preprocessing

The following preprocessing techniques were applied before training the models:

✔ Handling Categorical Features
Converted:
Sex → Male/Female → 0/1
Chest Pain Type → One-Hot Encoding
Resting ECG → One-Hot Encoding
✔ Boolean Conversion
Converted True/False values into 0/1
✔ Feature Scaling
Applied StandardScaler for normalization
✔ Data Preparation
Ensured all features were numeric for machine learning models
📊 Exploratory Data Analysis (EDA)

Several visualizations and analyses were performed to understand the dataset.

Key Insights
✔ Balanced Dataset
Heart Disease Present → 508
No Heart Disease → 410
✔ Important Correlations
exang → Positive correlation with heart disease
oldpeak → Strong indicator
thalch → Negative correlation
✔ Most Important Features
Chest pain type
Oldpeak
Maximum heart rate
🤖 Model Training

The following machine learning models were trained and evaluated:

Logistic Regression
Decision Tree
Random Forest
🔄 Training Process
Train-Test Split → 80/20
Feature Scaling using StandardScaler
Model Training
Model Evaluation
📈 Model Evaluation
Model	Accuracy
Logistic Regression	80.43%
Decision Tree	78.80%
Random Forest	82.60%
✔ Evaluation Metrics Used
Confusion Matrix
ROC-AUC Score
✔ ROC-AUC Score
Approximately 0.91
✅ Final Model Selection
Final Model: Logistic Regression

Although Random Forest achieved the highest accuracy (~82.6%), the project requirement allowed only Logistic Regression for final deployment.

Why Logistic Regression?
Stable and interpretable model
Good balance of precision and recall
Lightweight and efficient
Accuracy: 80.43%
🚀 Deployment (Streamlit App)

The project was deployed using Streamlit.

Saved Files
model.pkl
scaler.pkl
App Functionality

The user enters medical parameters, and the model predicts the heart disease risk.

Prediction Outputs
🚨 High Risk of Heart Disease
✅ No Heart Disease Risk
🖥️ Project Output
<img width="1779" height="707" alt="image" src="https://github.com/user-attachments/assets/8d18ed8b-ea4b-4793-849b-f324dd291a2f" />
<img width="1785" height="705" alt="image" src="https://github.com/user-attachments/assets/e60a0982-0256-4898-9b10-4e3933195df3" />

📌 Conclusion

This project demonstrates that machine learning can effectively predict heart disease risk using patient medical data.

Final Results
Random Forest achieved the best experimental accuracy (~82.6%)
Logistic Regression was selected as the final deployed model
Final deployment accuracy: 80.43%
Key Predictors
Chest pain type
Oldpeak
Maximum heart rate

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone <your-github-repository-link>
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit App
streamlit run app.py
📌 Future Improvements
Improve prediction accuracy using advanced ensemble models
Add AI chatbot support for better user interaction
Enhance UI/UX design
Add patient history tracking
Deploy the project online using Streamlit Cloud
