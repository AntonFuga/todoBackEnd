from flask import Flask
from resources import  new_entry
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p>"

@app.route("/test")
def hello_test():
    return new_entry.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)