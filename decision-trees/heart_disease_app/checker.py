import pandas as pd
import joblib

model = joblib.load("model/heart_disease_model.pkl")
trained_columns = joblib.load("model/trained_columns.pkl")

# Example input
values = {
    "age": 8.0,
    "sex": 1.0,
    "restbp": 112.0,
    "chol": 212.0,
    "fbs": 0.0,
    "thalach": 112.0,
    "exang": 1.0,
    "oldpeak": 2.3,
    "ca": 1.5,
    "cp": 2.0,
    "restecg": 1.0,
    "slope": 2.0, 
    "thal": 6.0
}

df = pd.DataFrame([values])

for col in ['cp', 'restecg', 'slope', 'thal']:
    print(col, df[col].iloc[0], f"{col}_{df[col].iloc[0]}")
    print("Exists in trained_columns?", f"{col}_{df[col].iloc[0]}" in trained_columns)

# One-hot encode
df_encoded = pd.get_dummies(df)

# Reindex to match training columns
df_encoded = df_encoded.reindex(columns=trained_columns, fill_value=0)

# Predict
pred = model.predict(df_encoded)[0]
print(pred)
print("Prediction:", "Heart Disease" if pred == 1 else "No Heart Disease")
