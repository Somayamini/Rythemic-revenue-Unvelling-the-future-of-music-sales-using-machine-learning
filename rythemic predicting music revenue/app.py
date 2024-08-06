import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('xgb.pkl', 'rb'))
# scale = pickle.load(open(r'scale.pkl', 'rb'))

@app.route('/')  # Rendering the HTML template
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/inner_page')  # Rendering the HTML template
def inner_page():
    return render_template("inner_page.html")

@app.route('/submit', methods=["POST"])  # Route to show the predictions in a web UI
def submit():
    # Reading the input given by the user
    input_feature = [float(request.form.get("format")), float(request.form.get("year")), float(request.form.get("metric"))]
    input_feature = [np.array(input_feature)]
    names = ['Format', 'Year', 'Metric']
    data = pandas.DataFrame(input_feature, columns=names)

    # data_scaled = scale.fit_transform(data)
    # data = pandas.DataFrame(columns=names)
    
    # Predictions using the loaded model
    prediction = model.predict(data)
    out = prediction[0]
    return render_template("output.html", result=out)  # Showing the prediction results in a UI

if __name__ == "__main__":
    app.run(port=8000, debug=True)  # Running the app