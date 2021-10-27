# ScriptName: my_functions.py
# Author: Gabe 
# template for calling functions in another file def print_function(): print("I'm in another file :)")



def seperated_input(param1, param2, sepr=" ", endr="\n"):
    """
    this function is a print statement with some makeup on
    """
    print(param1.capitalize(), param2.capitalize(), sep=sepr, end=endr)


def three_numbers(number_1, number_2, number_3):
    """
    Function that checks if three numbers are equal to one another and returns True if they are
    """

    if (number_1 == number_2) and (number_2 == number_3):
        return True

    else:
        return False


def seasons(number):
    """
    THis function asks the user for a number and returns the corrosponding seasons, also responds with an error if the wrong number is entered
    """
#    number = input("Plz give me  a number between 1 and 4:  ")
    try:
            
        if number > 4 or number < 1:
            print("Number entered", number, "is outside of input values")

        elif number == 1:
            print("Winter")

        elif number == 2:
            print("Spring")

        elif number == 3:
            print("Summer")

        elif number == 4:
            print("Autumn")

    except TypeError:
        print("Please input a number babes")

def grades(number):
    if number in range(85, 100):
        print("Congrats you got an A!")

    elif number in range(70, 84):
        print("Not bad,you got a B")

    elif number in range(55, 66):
        print("Eh, a C isn't awful I guess...")

    elif number in range(40, 54):
        print("This is disappointing, a D????")

    elif number in range(25, 39):
        print("You disgust me, you got an E")

    elif number in range(0 , 4):
        print("HOW DARE YOU?? AN F??")
