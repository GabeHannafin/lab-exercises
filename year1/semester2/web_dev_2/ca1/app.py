from flask import Flask, render_template, session, request, url_for, redirect, g
from database import get_db, close_db
from forms import LoginForm, OrderForm, NewHitman
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

"""
two users are available:
    username: admin, password:admin
    username: ghost, password:boo

the datefield in the order page doesnt seem to work correctly on the server
but running locally in the same browser it does so i assume it's something 
to do with the server

enjoy :)
"""



app = Flask("__name__")
app.config["SECRET_KEY"] = "YWwiSPcGWTWrGxpjawOYkoNgULkiaBMgdUUhXbKsfPEMfNOokYFjcvbFAPgj"
app.teardown_appcontext(close_db)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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
    next_button = False
    if "orders" not in session:
        session["orders"] = {}
    if "chosen_hitman" not in session:
        session["chosen_hitman"] = False

    if session["chosen_hitman"] != False:
        next_button = True
    hitmen = db.execute("""SELECT * FROM hitmen""").fetchall()
    return render_template("index.html", next_button=next_button,orders=session["orders"], number=session["chosen_hitman"]-1, hitmen=hitmen)

@app.route("/order", methods=["GET", "POST"])
def order():
    if "orders" not in session:
        session["orders"] = {}
    orders = session["orders"]
    db = get_db()
    form = OrderForm()
    order_number= len(session["orders"])
    status = "HUNTING"
    if form.validate_on_submit():
        order_number +=1
        orders[order_number] = {}
        orders[order_number]["target_name"] = form.target.data
        orders[order_number]["status"] = status

        orders[order_number]["suffering"] = form.suffering.data

        return redirect(url_for("index"))
    hitmen = db.execute("""SELECT * FROM hitmen""").fetchall()

    return render_template("order.html", form=form, number=session["chosen_hitman"]-1, hitmen=hitmen)

@app.route("/status")
def status():
    return render_template("status.html")

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
    session.pop("username")
    session.pop("chosen_hitman")
    return redirect( url_for("index") )


@app.route("/add_to_cart/<int:hitman_id>")
@login_required
def add_to_cart(hitman_id):
    if "chosen_hitman" not in session:
        session["chosen_hitman"] = 0
    session["chosen_hitman"] = int(hitman_id)
    return redirect( url_for("index") )

@app.route("/remove_hitman/<int:hitman_id>")
@login_required
def remove(hitman_id):
    if g.user != "admin":
        return render_template("403.html")
    db = get_db()
    db.execute("""DELETE FROM hitmen WHERE id==?;""", (hitman_id,))
    db.commit()
    session.pop("chosen_hitman")
    return redirect(url_for("index"))


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    form = NewHitman()
    db = get_db()
    if g.user != "admin":
        return render_template("403.html")
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        db.execute("""INSERT INTO hitmen(name, description)
                     VALUES (?,?);""", (name,description))
        db.commit()
        return redirect(url_for("index"))
    return render_template("admin.html", form=form)
