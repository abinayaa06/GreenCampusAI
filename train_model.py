import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("campus_dataset.csv")

X = data[
    ["electricity", "water", "waste", "students"]
]

y = data["risk"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(
    model,
    "campus_model.pkl"
)

print("Model trained successfully")