from flask import Flask, render_template
from forms import CaesarForm, HotForm



app = Flask("__name__")

app.config["SECRET_KEY"] = "bleeeeeeeeeeeeeeeeeeeeeeeeeeep"


@app.route("/shift", methods=["GET", "POST"])
def caesar():
    # get the form and save it to a variable
    form = CaesarForm()
    # if the method is a post request
    if form.validate_on_submit():
        # get the plaintext data
        plaintext= form.plaintext.data
        # Get the shift data
        shift = form.shift.data
        # Code for conversion
        ciphertext = ""
        for char in plaintext:
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char
        # add the answer to the form
        form.ciphertext.data = ciphertext        
    # return the form page
    return render_template("shift_form.html", form=form)


@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    # Get the form
    form = HotForm()
    # If method is post
    if form.validate_on_submit():
        # Get the data from the form
        input_number = form.input_field.data
        conversion_from = form.from_field.data
        conversion_to = form.to_field.data
        # convert the temps
        if conversion_from == "Celsius" and conversion_to == "Fahrenheit" :
            answer =  9/5 * input_number + 32
        elif conversion_from == "Kelvin" and conversion_to == "Fahrenheit" :
            answer = 9/5 * (input_number - 273) + 32
        elif conversion_from == "Fahrenheit" and conversion_to == "Celsius" :
            answer = 5/9 * (input_number - 32)
        elif conversion_from == "Celsius" and conversion_to == "Kelvin" :
            answer = input_number + 273
        elif conversion_from == "Kelvin" and conversion_to == "Celsius" :
            answer = input_number - 273 
        elif conversion_from == "Fahrenheit" and conversion_to == "Kelvin" :
            answer = 5/9 * (input_number - 32) + 273
        else:
            answer = input_number
        # add the answer to the form
        form.answer_field.data = answer


    # return the form and the answer
    return render_template("hot_form.html", form=form)
