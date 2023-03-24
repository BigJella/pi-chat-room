from flask import Flask
from API import auth_required

app = Flask(__name__, static_url_path='', static_folder="static")

@auth_required
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"