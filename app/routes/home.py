from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/")
def index():
    return render_template("pages/home.html")

@home.route("/solutions/")
def solutions():
    return render_template("pages/solutions.html")

@home.route("/concepts/")
def concepts():
    return render_template("pages/concepts.html")