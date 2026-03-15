from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["medinc"]),
        float(request.form["houseage"]),
        float(request.form["averooms"]),
        float(request.form["avebedrms"]),
        float(request.form["population"]),
        float(request.form["aveoccup"]),
        float(request.form["latitude"]),
        float(request.form["longitude"])
    ]

    prediction = model.predict([features])[0]

    # Optional: convert to rupees/lakhs
    prediction = round(prediction * 100000, 2)

    return render_template("result.html", price=prediction)

if __name__ == "__main__":
    app.run(debug=True)
