from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField
from wtforms.validators import InputRequired, NumberRange



class CaesarForm(FlaskForm):

    plaintext = StringField("Plaintext: ", validators=[InputRequired()])
    shift = IntegerField("Shift: ", validators=[NumberRange(1, 25)])
    ciphertext = StringField("Ciphertext: ")
    submit = SubmitField()

class HotForm(FlaskForm):

    from_field = RadioField(choices=["Fahrenheit", "Celsius", "Kelvin"], default="Kelvin")
    input_field = IntegerField(validators = [InputRequired()])

    to_field = RadioField(choices=["Fahrenheit", "Celsius", "Kelvin"], default="Kelvin")
    answer_field = StringField()
    submit = SubmitField()
