from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return "vijay"

if __name__ == "__main__":
    app.run(debug=True)
