from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired



class EuroForm(FlaskForm):
    country = StringField("Country: ", validators=[InputRequired()])
    submit = SubmitField()

class MinWinForm(FlaskForm):
    country = StringField("Country: ")
    points = StringField("Points: ")
    submit = SubmitField()
