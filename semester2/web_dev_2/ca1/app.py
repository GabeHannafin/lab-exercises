from flask import Flask, render_template, session
from database import get_db, close_db
from flask_session import Session



app = Flask("__name__")
app.config["SECRET_KEY"] = "YWwiSPcGWTWrGxpjawOYkoNgULkiaBMgdUUhXbKsfPEMfNOokYFjcvbFAPgj"
app.teardown_appcontext(close_db)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
