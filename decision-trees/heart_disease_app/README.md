# Heart Disease Prediction Web App ❤️

This is a simple web application that predicts whether a person is likely to have heart disease using a trained Decision Tree model.

## Features

- Input patient data through a web form:
  - Age, Sex, Chest Pain type, Resting Blood Pressure, Cholesterol, etc.
- Predict if a person has heart disease using a trained model (`DecisionTreeClassifier`).
- Display the result dynamically on the webpage.
- Backend: Flask
- Frontend: HTML + CSS
- Machine Learning Model: Scikit-learn Decision Tree, saved as `.pkl`

## Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd heart_disease_app

2. Install dependencies:

pip install -r requirements.txt


3. Run the app:

python app.py


4. Open your browser at http://127.0.0.1:5000

## File Structure
heart_disease_app/
├── model/
│   └── heart_disease_model.pkl
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md


the mdoel was trained in the google colab 