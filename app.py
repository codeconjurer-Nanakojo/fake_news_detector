from flask import Flask, render_template, request
import joblib
# initialise the app
app = Flask(__name__)

# load the model
model = joblib.load('trained_model.pkl')
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        text = request.form['news']
        prediction = model.predict([text])[0]
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
