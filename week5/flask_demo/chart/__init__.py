from flask import Flask

app = Flask(__name__)
app.secret_key = "some random value"

# necessary to get the routes registered
import chart.views