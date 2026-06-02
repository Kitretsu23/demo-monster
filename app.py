from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello the app is working fine!"

@app.route('/about')
def about():
    return "Flask is running yayaaeee!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)