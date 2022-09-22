from flask import Flask, render_template
from database import get_db, close_db



app = Flask("__name__")
app.config["SECRET_KEY"] = "YWwiSPcGWTWrGxpjawOYkoNgULkiaBMgdUUhXbKsfPEMfNOokYFjcvbFAPgj"
app.teardown_appcontext(close_db)

