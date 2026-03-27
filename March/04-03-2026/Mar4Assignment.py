'''
Project: Loan Approval Predictor

Dataset columns:

Income

Credit Score

Age

Loan Amount

Employment Years

Steps:

Load dataset

Train Decision Tree

Train Random Forest

Compare accuracy

Show feature importance

Save model using pickle
'''

# Loan Approval Predictor

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
data = pd.read_csv("loan_data.csv")
X = data[["Income", "Credit Score", "Age", "Loan Amount", "Employment Years"]]
y = data["Loan Approved"]   # 1 = Approved, 0 = Not Approved
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)

print("Decision Tree Accuracy:", dt_accuracy)
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
print("Random Forest Accuracy:", rf_accuracy)




importance = rf_model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", score)




with open("loan_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)

print("Model saved as loan_model.pkl")