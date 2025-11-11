from flask import Flask

# To execute (in this directory): flask --app hello run
#


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
