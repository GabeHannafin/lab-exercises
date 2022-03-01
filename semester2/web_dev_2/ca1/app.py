from flask import Flask, render_template, session, request, url_for, redirect, g
from database import get_db, close_db
from forms import LoginForm
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps



app = Flask("__name__")
app.config["SECRET_KEY"] = "YWwiSPcGWTWrGxpjawOYkoNgULkiaBMgdUUhXbKsfPEMfNOokYFjcvbFAPgj"
app.teardown_appcontext(close_db)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.before_request
def load_logged_in_users():
    g.user = session.get("username", None)


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for("login", next=request.url))
        return view(**kwargs)
    return wrapped_view


@app.route("/")
def index():
    db = get_db()
    hitmen = db.execute("""SELECT * FROM hitmen""").fetchall()
    return render_template("index.html", hitmen=hitmen)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    db = get_db()
    if form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data

        check_user = db.execute("""SELECT * FROM users WHERE username==?;""", (user_name,)).fetchone()

        if not check_user:
            form.user_name.errors.append("Incorrect Credentials!")
        elif not check_password_hash(check_user["password"], password):
                form.user_name.errors.append("Incorrect Credentials!")
        else:
            session.clear()
            session["username"] = user_name
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login.html", form=form) 

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect( url_for("index") )

@app.route("/violence")
@login_required
def protected():
    return "sex"
