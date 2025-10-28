import pickle as pkl
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
import numpy as np
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

with open(r'C:\Users\Abdullahi Mujaheed\Desktop\mlzoom\mlzoomcamp\pipleine.bin', 'rb') as f_out:
    dv, model = pkl.load(f_out)

class InputData(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float
@app.post('/mod5_deployment')
def trans_predict(input_data: InputData):
    client = input_data.dict()
    prediction = model.predict_proba(dv.transform(client))
    return prediction