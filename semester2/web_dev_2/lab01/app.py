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
    # Dict to convert random number to hand
    random_hand = {1 : "rock", 2: "paper", 3: "scissors"}
    # Dict to compare hands
    beats = {"rock": "scissors", "paper":"rock", "scissors":"paper"}

    # if the input is in the dictionary
    if player.lower() in beats:
        #generate computer hand
        computer_result = random_hand[randint(1, 3)]
        #Compare the hands
        if beats[player.lower()] == computer_result:
            outcome = "Player Wins!"
        elif player.lower() == computer_result:
            outcome = "It's a draw!"
        else:
            outcome = "Computer Wins!"
        # return the success page
        return render_template("rps.html", outcome=outcome, player=player, computer=computer_result) 
    else:
        # return the error page
        outcome = "That is not a valid hand"
        return render_template("error.html", outcome=outcome)



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





@app.route("/rps15/<player>")
def rps15(player=None):
    """
    1 = rock
    2 = paper
    3 = sneezors
    """
    # Dict to convert random number to hand
    random_hand = {1 : "rock", 2: "fire", 3: "scissors", 4: "snake", 5:"human", 6:"tree", 7:"wolf", 8:"sponge", 9:"paper", 10: "air", 11: "water", 12:"dragon", 13:"devil", 14:"lightning", 15:"gun"}
    # Dict to compare hands
    beats = {
            "rock": ["fire", "scissors", "snake", "human", "wolf", "sponge", "tree"],
            "fire": ["scissors", "paper", "snake", "human", "tree", "wolf", "sponge"],
            "scissors": ["air", "tree", "paper", "snake", "human", "wolf", "sponge"],
            "snake": ["human", "wolf", "sponge", "tree", "paper", "air", "water"],
            "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
            "tree": ["wolf", "dragon", "sponge", "paper", "air", "water", "devil"],
            "wolf": ["sponge", "paper", "air", "water", "dragon", "lightning", "devil"],
            "sponge": ["paper", "air", "water", "devil", "dragon", "gun", "lightning"],
            "paper": ["air", "rock", "water", "devil", "dragon", "gun", "lightning"],
            "air": ["fire", "rock", "water", "devil", "gun", "dragon", "lightning"],
            "water": ["devil", "dragon", "rock", "fire", "scissors", "gun", "lightning"],
            "dragon": ["devil", "lightning", "fire", "rock", "scissors", "gun", "snake"],
            "devil": ["rock", "fire", "scissors", "gun", "lightning", "snake", "human"],
            "lightning": ["gun", "scissors", "rock", "tree", "fire", "snake", "human"],
            "gun": ["rock", "tree", "fire", "scissors", "snake", "human", "wolf"]
            }

    # if the input is in the dictionary
    if player.lower() in beats:
        #generate computer hand
        computer_result = random_hand[randint(1, 15)]
        # Iterate through every item in the list of hands the computer hands beats
        for item in beats[computer_result]:
            # if player and computer hands are the same then it is a draw
            if player.lower() == computer_result:
                outcome = "It's a draw!"
            # if the player hand is equal to any item in the list then it is beaten by the computer
            elif player.lower() == item:
                outcome = "Computer Wins!"
                # have to break the loop otherwise the outcome variable is overwritten
                break
            # If it is not in the list then the Player must have won
            elif player.lower() != item:
                outcome = "Player Wins!"
        # return the success page
        return render_template("rps.html", outcome=outcome, player=player, computer=computer_result) 
    else:
        # return the error page
        outcome = "That is not a valid hand"
        return render_template("error.html", outcome=outcome)

