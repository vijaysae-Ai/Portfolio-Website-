from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("Resume.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/nlp_project')
def nlp_project():
    return render_template("nlp_project.html")

@app.route('/movie_recommendation')
def movie_recommendation():
    return render_template("movie_recommendation.html")

@app.route('/fraud_detection')
def fraud_detection():
    return render_template("fraud_detection.html")

@app.route('/customer_churn_prediction')
def customer_churn_prediction():
    return render_template("customer_churn_prediction.html")

@app.route('/nlp_for_customer_support')
def nlp_for_customer_support():
    return render_template("nlp_for_customer_support.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
