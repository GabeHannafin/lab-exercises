from flask import Flask, render_template
from random import randint


app = Flask("__name__")

@app.route("/rps/<player>")
def rps(player=None):
    """
    1 = rock
    2 = paper
    3 = sneezors
    """
    # Dict to compare hands
    beats = {"rock": "scissors", "paper":"rock", "scissors":"paper"}

    # if the input is in the dictionary
    if player.lower() in beats:
    #generate computer hand
        computer_result = randint(1, 3)
        # assign the correct value to the result
        if computer_result == 1:
            computer_result = "rock"

        elif computer_result == 2:
            computer_result = "paper"

        elif computer_result == 3:
            computer_result = "scissors"

        if beats[player.lower()] == computer_result:
            outcome = "Player Wins!"

        elif player.lower() == computer_result:
            outcome = "It's a draw!"

        else:
            outcome = "Computer Wins!"
    else:
        outcome = "That is not a valid hand"

    return render_template("rps.html", outcome=outcome, player=player, computer=computer_result) 


@app.route("/could_it_be_me/<amount_of_lines>")
def send_lotto_numbers(amount_of_lines):
    try:
        # cast input to int
        amount_of_lines = int(amount_of_lines)
        # create list to contain all lotto numbers
        all_lines = []
        # first for loop to create the needed amount of lines
        for i in range(amount_of_lines):
            # create list to store numbers
            line = []
            # Accumulator to continue to generate numbers until there are 6 unique numbers
            total = 0
            # generating the 6 numbers
            while total < 6:
                # pick random number
                n = randint(1, 47)
                # only append to the list if the list does not already contain that number
                if n not in line:
                    line.append(n)
                    # add 1 to the total amount acumulator
                    total +=1
            # append the resulting list to the big list
            all_lines.append(line)
        # render the page
        return render_template("lotto.html", line=all_lines)
    # basic error handling
    except Exception:
        return "Please input an interger"





