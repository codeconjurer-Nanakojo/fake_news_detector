from flask import Flask, render_template, request
import joblib
import numpy as np
import re

app = Flask(__name__)

model = joblib.load("trained_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Map numeric predictions to labels
label_map = {0: "FAKE", 1: "REAL"}


def get_top_keywords(text, vectorizer, top_n=5):
    vectorized = vectorizer.transform([text])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_array = vectorized.toarray()[0]
    top_indices = tfidf_array.argsort()[-top_n:][::-1]
    keywords = [(feature_names[i], tfidf_array[i]) for i in top_indices if tfidf_array[i] > 0]
    return keywords


def highlight_word(text, word):
    pattern = re.compile(rf'\b({re.escape(word)})\b', re.IGNORECASE)
    return pattern.sub(r'<mark>\1</mark>', text)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    highlighted_preview = None
    input_text = ""

    if request.method == "POST":
        try:
            input_text = request.form["news"]
            if input_text:
                vectorized_text = vectorizer.transform([input_text])
                raw_prediction = model.predict(vectorized_text)[0]
                prediction = label_map.get(raw_prediction, "Unknown")

                proba = model.predict_proba(vectorized_text)[0]
                confidence = round(np.max(proba) * 100, 2)

                keywords = get_top_keywords(input_text, vectorizer, top_n=7)
                highlighted_preview = input_text
                keywords_sorted = sorted(keywords, key=lambda x: len(x[0]), reverse=True)

                for word, _ in keywords_sorted:
                    highlighted_preview = highlight_word(highlighted_preview, word)

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        highlighted_preview=highlighted_preview,
        input_text=input_text,
    )


if __name__ == '__main__':
    app.run(debug=True, port=5001)
