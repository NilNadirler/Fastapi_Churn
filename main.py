from fastapi import FastAPI
import pickle
from schemas import Customer

app=FastAPI()
model= pickle.load(open("model.pkl","rb"))

@app.get("/")
def home():
    return {"message": "ok"}

@app.post("/predict")
def predict(data:Customer):
    values= [
        data.Tenure_in_Months,
        data.Monthly_Charge,
        data.Total_Charges,
    ]
    pred= model.predict([values])[0]
    prob= model.predict_proba([values])[0][1]

    if prob>0.8:
        segment="High Risk"
    elif prob>0.6:
        segment="Medium"
    else:
        segment="Low Risk"


    return {
        "prediction": int(pred),
        "churn_probability": float(prob),
        "segment": segment
    }