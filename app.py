from flask import Flask, render_template, request
import joblib
import numpy as np
from feature_extraction import extract_features

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    url = request.form.get("url")

    try:
        # Extract features from URL
        features = extract_features(url)

        # Convert features to numpy array
        features = np.array(features, dtype=float).reshape(1, -1)

        # Prediction
        prediction = model.predict(features)[0]

        # Dataset label mapping:
        # 1 = Legitimate
        # 0 = Phishing
        if prediction == 1:
            result = "Likely Legitimate Website ✅"
        else:
            result = "Possible Phishing Website ⚠️"

        return render_template(
            "result.html",
            result=result,
            url=url
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)