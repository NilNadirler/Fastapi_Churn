import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv("telco.csv")

df["Churn Label"] = df["Churn Label"].map({"Yes":1, "No":0})

features = ["Tenure in Months", "Monthly Charge", "Total Charges"]

X = df[features].copy()
y = df["Churn Label"]

X["Total Charges"] = pd.to_numeric(X["Total Charges"], errors="coerce")
X = X.fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

pickle.dump(pipeline, open("model.pkl", "wb"))

