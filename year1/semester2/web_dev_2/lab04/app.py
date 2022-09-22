from flask import Flask, render_template
from forms import EuroForm, MinWinForm
from database import get_db, close_db



app = Flask("__name__")

# Setup flask
app.config["SECRET_KEY"] = "bleeeeeeeeeeeeeeeeeeeeeeeeeeep"
app.teardown_appcontext(close_db)


@app.route("/winners", methods=["GET", "POST"])
def winners():
    # initialise results
    results = None
    # get the form and save it to a variable
    form = EuroForm()
    # if the method is a post request
    if form.validate_on_submit():
        # grab the user input
        country = form.country.data.capitalize()
        # initialise the db
        db = get_db()
        # query the database and grab all matching country data
        results = db.execute("""SELECT * FROM winners WHERE country == ?;""", (country,)).fetchall()
        # if there are no results
        if not results:
            # add a new error
            form.country.errors.append("Country not found")
        # render the template
    return render_template("euro.html", form=form, results=results)

@app.route("/min_winners", methods=["GET", "POST"])
def min_winners():
    # Initialise results
    results = None
    # get the form
    form = MinWinForm()
    # if is a post request
    if form.validate_on_submit():
        # initialise the database
        db = get_db()
        # grab both user inputs
        points = form.points.data
        country = form.country.data.capitalize()
        # if just country
        if country and not points:
             # get all results for country
             results = db.execute("""SELECT * FROM winners WHERE country ==?; """, (country,)).fetchall()
        # if just points
        elif points and not country:
             # get everything with at least that amount of points
             results = db.execute("""SELECT * FROM winners WHERE points >=?; """, (points,)).fetchall()
        # if both of them
        elif points and country:
             # get all the winners from the country with at lesst <points> amount of points
             results = db.execute("""SELECT * FROM winners WHERE country == ? AND points >=?; """, (country,points,)).fetchall()
        # if nothing supplied
        else:
             # get everything
             results = db.execute("""SELECT * FROM winners""").fetchall()
    # render the form
    return render_template("min_winners.html", form=form, results=results)
