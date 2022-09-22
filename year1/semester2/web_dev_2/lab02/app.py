from flask import Flask, render_template, request



app = Flask("__name__")

@app.route("/spy", methods=["GET", "POST"])
def spy():
    # return the form when a GET request is sent
    if request.method == "GET":
        return render_template("spy_form.html")
    else:
        # get the information from the form
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        # return the correct response
        return render_template("spy_result.html", first=given_name, last=family_name)


@app.route("/morse", methods=["GET", "POST"])
def morse():
    # return the form when a GET request is sent
    if request.method == "GET":
        return render_template("morse_form.html", error="")
    else:
        # get the message from the form
        message = request.form["message"]
        # if the user doesn't enter any data then return an error message
        if message == "":
            return render_template("morse_form.html", error="Please enter a message")

        # dictionary containing all the needed characters
        morse = ""
        morse_dict = { 
            'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-',
            ' ':'/'
            }

        try:
            # encode every character
            for char in message:
                # append it to the morse string
                morse += morse_dict[char.upper()] + " "
        # if there is an error return an error message
        except Exception:
            return render_template("morse_form.html", error="THAT CHARACTER IS INVALID >:(")
        # return the output
        return render_template("morse_response.html", message=message, morse=morse)

@app.route("/lengths", methods=["GET", "POST"])
def lengths():
    if request.method == "GET":
        return render_template("length_form.html")
    else:
        # get the form data
        centimetres = request.form["centimetres"]
        inches = request.form["inches"]
        # if there is a value in inches and centimetres is empty then convert the inches
        if inches != "" and centimetres == "":
            # converting the number
            answer = float(inches) * 2.54
            # return the answer
            return render_template("length_form.html", answer=answer)
        # if there is a value in centimetres only then do the conversion to inches
        elif inches == "" and centimetres != "":
            # converting the number
            answer = float(centimetres) / 2.54
            # returning the answer
            return render_template("length_form.html", answer=answer)
        # if neither of these are true, i.e both empty or full then give an error
        else:
            return render_template("length_form.html", error="I hate you")

