from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Here is the top page."

@app.route("/hello")
def hello():
    return "Hello World! What’s new?"

if __name__ == "__main__":
    app.run(debug=True)
