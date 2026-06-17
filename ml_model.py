import joblib
import pandas as pd

model = joblib.load(
    "campus_model.pkl"
)

def predict_risk(
    electricity,
    water,
    waste,
    students
):

    data = pd.DataFrame({
        "electricity": [electricity],
        "water": [water],
        "waste": [waste],
        "students": [students]
    })

    prediction = model.predict(data)[0]

    return prediction