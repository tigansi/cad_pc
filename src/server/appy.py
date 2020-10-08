from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return ""
