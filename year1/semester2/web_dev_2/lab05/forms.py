from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField


class GuessForm(FlaskForm):
    user_guess = IntegerField("Your Guess: ")
    submit = SubmitField()


