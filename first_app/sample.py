import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!To the First page"

@app.route('/How Covid')
def hello():
    return 'I am good, what about your situation?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)