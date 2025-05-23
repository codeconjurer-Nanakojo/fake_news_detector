from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load("trained_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Label mapping for predictions
label_map = {0: "FAKE", 1: "REAL"}


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    if request.method == "POST":
        try:
            text = request.form.get("news", "").strip()
            if not text:
                error = "Please enter news text to analyze."
            else:
                vectorized_text = vectorizer.transform([text])
                pred_class = model.predict(vectorized_text)[0]
                prediction = label_map.get(pred_class, "Unknown")
        except Exception as e:
            error = f"Error during prediction: {str(e)}"

    return render_template("index.html", prediction=prediction, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
