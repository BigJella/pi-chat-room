from flask import Flask

app = Flask(__name__, static_url_path='', static_folder="static")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"