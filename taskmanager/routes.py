from flask import render_template
from taskmanager import app, db
from taskmanager.models import Categorty, Task


@app.route("/")
def home():
    return render_template("base.html")
