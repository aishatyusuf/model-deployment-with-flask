from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(APP_ROOT, "model.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template("index.html", prediction_text = "The predicted score is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)