from flask import Flask, render_template, session
from forms import GuessForm
from flask_session import Session
from random import randint


# config
app = Flask("__name__")

app.config["SECRET_KEY"] = "YWwiSPcGWTWrGxpjawOYkoNgULkiaBMgdUUhXbKsfPEMfNOokYFjcvbFAPgj"
# Session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/guess", methods=["GET", "POST"])
def guess():
    # if no number present in session gen one
    if "number" not in session:
        session["number"] = randint(1,100)
    # initialise variable
    message = ""
    # get form
    form = GuessForm()
    # if post request
    if form.validate_on_submit():
        # get the user input
        user_guess = form.user_guess.data
        # compare the numbers
        if user_guess > session["number"]:
            message = "You're too high"
        elif user_guess < session["number"]:
            message = "You're too low"
        else:
            message = "You got it!!"
    # render the page
    return render_template("guess.html", form=form, message=message) 
