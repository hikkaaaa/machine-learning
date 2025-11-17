from flask import Flask, render_template, request
import joblib 
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/heart_disease_model.pkl")
trained_columns = joblib.load("model/trained_columns.pkl") #list of columns, since due to one-hot encoding, it needs more than 14 usual features

@app.route("/", methods=["GET", "POST"])
def index():
    values = {}
    prediction = None
    if request.method == "POST":
        values = request.form.to_dict()
        for k in values:
           values[k] = float(values[k])
        df = pd.DataFrame([values])
        
        for col in ['cp', 'restecg', 'slope', 'thal']:
            df[col] = df[col].astype(str) + ".0"

        df_encoded = pd.get_dummies(df)
        df_encoded = df_encoded.reindex(columns=trained_columns, fill_value=0)
    
        try:
            pred_value = model.predict(df_encoded)[0]
            
            if pred_value == 1:
                prediction = "Person is likely to have Heart Disease"
            else:
                prediction = "Person is unlikely to have Heart Disease"
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template("index.html", values = values, prediction = prediction)

if __name__ == "__main__": 
    app.run(debug = True)