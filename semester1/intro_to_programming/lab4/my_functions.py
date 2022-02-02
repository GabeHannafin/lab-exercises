# ScriptName: my_functions.py
# Author: Gabe 
# template for calling functions in another file def print_function(): print("I'm in another file :)")

import math

def seperated_input(param1, param2, sepr=" ", endr="\n"):
    """
    this function is a print statement with some makeup on
    """
    param1_cap = str(param1).capitalize()
    param2_cap = str(param2).capitalize()

    print(param1_cap, param2_cap, sep=sepr, end=endr)


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
    Write a function called seasons(), that has a parameter called number.
    Ask the user for a  number, and pass this number to the function.
    Depending on the number passed to the function, the function will return
    the corresponding season of the year where 1=Winter, 2=Spring, 3=Summer, and 4
    = Autumn.  Add code to returnan error message if any other number is
    entered
    """
    if type(number) != int:    
            print("Input value must be a number")

    elif number > 4 or number < 1:
        print("Number entered", number, "is outside of input values")

    elif number == 1:
        print("Winter")

    elif number == 2:
        print("Spring")

    elif number == 3:
        print("Summer")

    elif number == 4:
        print("Autumn")


def grades(number):
    '''
    Write a function called seasons(), that has a parameter called number.
    Ask the user for a  number, and pass this number to the function.
    Depending on the number passed to the function, the function will return
    the corresponding season of the year where
    1=Winter, 2=Spring, 3=Summer, and 4 = Autumn.
    Add code to return an error message if any other number is entered:
    '''

    # Check if the an int is specified
    if type(number) != int:
            print("Input value must be a number")

    elif number < 0 or number > 100:
            print("X")

    elif number in range(85, 100):
            print("A")

    elif number in range(70, 84):
            print("B")

    elif number in range(55, 66):
            print("C")

    elif number in range(40, 54):
            print("D")

    elif number in range(25, 39):
            print("E")

    elif number in range(0 , 4):
            print("F")


def equal_numbers(number_1, number_2):
    '''
    Ask the user for 2 numbers, and pass these 2 numbers to a function called equal_numbers().
    If the two numbers are equal, then return the square root ofthe number as a float
    (Use import mathat the top of your program to import the math library and use the command math.sqrt()
    e.g math sqrt (25.0) gives 5.0).
    If the two numbers are not equal, then return the squares of both numbers as integers.
    '''
        # Error handling: check if type is int
    if type(number_1) != int or type(number_2) != int:
            print("Input value(s) must be a number")

    elif (number_1 == number_2):
            answer_float = float(math.sqrt(number_1))
            return answer_float

    elif (number_1 != number_2):
            answer1_int = int(number_1 ** 2)
            answer2_int = int(number_2 ** 2)    
            return (answer1_int, answer2_int)
