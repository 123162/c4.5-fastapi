# import library
from fastapi import FastAPI, UploadFile, File
from model.tree_model import DecisionTreeClassifier
import pandas as pd
import numpy as np
from io import BytesIO

app = FastAPI()#activate fastAPI
model = None

@app.post("/train")
async def train_model(file: UploadFile = File(...), max_depth: int = 3, min_samples_split: int = 3):
    contents = await file.read()
    df = pd.read_excel(BytesIO(contents))

    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values.reshape(-1, 1)

    global model
    model = DecisionTreeClassifier(min_samples_split=min_samples_split, max_depth=max_depth)
    model.fit(X, Y)

    return {"message": "Model trained successfully."}

@app.post("/predict")
async def predict(data: list[list[float]]):
    global model
    if model is None:
        return {"error": "Model is not trained yet."}

    prediction = model.predict(data)
    return {"prediction": prediction}
