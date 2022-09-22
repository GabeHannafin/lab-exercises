from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, TextAreaField, IntegerField, DateField
from wtforms.validators import InputRequired



class LoginForm(FlaskForm):
    user_name = StringField("Username:   ", validators=[InputRequired()]) 
    password = PasswordField("Password:    ", validators=[InputRequired()]) 
    submit = SubmitField()

class OrderForm(FlaskForm):
    target = StringField("Your target: ", validators=[InputRequired()])
    address = StringField("Target's Eircode: ", validators=[InputRequired()])
    suffering = BooleanField("suffering?: ", default=False)
    ppsn = StringField("Your PPSN: ", validators=[InputRequired()])
    your_name = StringField("Name on card: ", validators=[InputRequired()])
    card_number = IntegerField("Your card number: ", validators=[InputRequired()])
    expiry_date = DateField("Card expiry date: ", validators=[InputRequired()])
    cvv = IntegerField("CVV: ", validators=[InputRequired()])
    submit = SubmitField()

class NewHitman(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    description = TextAreaField("A short description for your lover?", render_kw={"rows":10, "cols":60}, validators=[InputRequired()])
    submit = SubmitField()



