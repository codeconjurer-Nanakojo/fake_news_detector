import joblib

# Load the model and vectorizer
model = joblib.load("trained_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Define the label mapping (edit this if your labels are different)
label_map = {
    0: "FAKE",
    1: "REAL"
}

def predict_news(text):
    try:
        text = text.strip()
        vectorized_text = vectorizer.transform([text])
        prediction = model.predict(vectorized_text)[0]
        return label_map.get(prediction, "Unknown")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("🧠 Fake News Detection Test Terminal")
    print("------------------------------------")
    while True:
        user_input = input("\nEnter a news sentence (or type 'exit' to quit):\n> ")
        if user_input.lower() == "exit":
            print("Exiting. Bye!")
            break
        result = predict_news(user_input)
        print(f"Prediction: {result}")
