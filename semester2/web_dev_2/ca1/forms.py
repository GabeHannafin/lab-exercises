from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    user_name = StringField("Username:   ", validators=[InputRequired()]) 
    password = PasswordField("Password:    ", validators=[InputRequired()]) 
    submit = SubmitField()

