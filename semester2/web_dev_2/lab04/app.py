from flask import Flask, render_template
from forms import EuroForm
from database import get_db, close_db


app = Flask("__name__")
app.config["SECRET_KEY"] = "cheese-on-toast"
app.teardown_appcontext(close_db)


@app.route("/winners", methods=["GET", "POST"])
def winners():
    form = EuroForm()
    results = None

    if form.validate_on_submit:
        country = form.country.data
        db = get_db()
        results = db.execute("""SELECT *
                      FROM winners
                      WHERE country=?;""", (country,)).fetchall()
        return render_template("euro.html", caption="Eurovision winners", form=form, results=results)

    return render_template("euro.html", form=form, results=results)
