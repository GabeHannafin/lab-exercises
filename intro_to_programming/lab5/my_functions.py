# ScriptName: my_functions.py
# Author: Gabe

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")

def fizz_buzz(num1, divisor_1=1, divisor_2=1):
    '''
    Pass a number, as parameter num1, to a function called fizz_buzz() For
    multiples of 3, return “Fizz”. For multiples of 5, return “Buzz”. For
    numbers which are multiples of both 3 and 5, e.g., 15, 30, etc, return
    “FizzBuzz”. If none of the conditions are true, simply return the number
    itself. Return the error statement 'Input value(s) must be a number’ when
    the inputs are not integers. Examples of what is returned by the function
    call are shown:
    '''
    '''
    a. If input is the wrong type the function throwns a type erro because it cannot do
        operations on a string
    b. Originally if num1 was not divisable by either divisor it returned none.
    '''

    # checking type for int
    try:
        if divisor_1 == 1 and divisor_2 == 1:

            if type(num1) != int:
                return "Input value(s) must be a number"

            elif (num1 % 3 == 0) and (num1 % 5 != 0):
                return "Fizz"

            elif (num1 % 5 == 0) and (num1 % 3 != 0):
                return "Buzz"

            elif ((num1 % 3 == 0) and (num1 % 5 == 0)):
                return "FizzBuzz"
            
            elif (num1 % 3 != 0 ) and (num1 % 5 != 0):
                return num1


        if divisor_1 != 1 and divisor_2 != 1:

            if (num1 % divisor_1 == 0) and (num1 % divisor_2 != 0):
                return "Fizz"

            elif (num1 % divisor_2 == 0) and (num1 % divisor_1 != 0):
                return "Buzz"

            elif (num1 % divisor_2 == 0) and (num1 % divisor_1 == 0):
                return "FizzBuzz"
            # When num1 is not divisable by either divisor return num1
            else:
                return num1

    except TypeError:
        return "Input value(s) must be a number'"

def grades(number):
    '''
    Write a function called seasons(), that has a parameter called number.
    Ask the user for a  number, and pass this number to the function.
    Depending on the number passed to the function, the function will return
    the corresponding season of the year where
    1=Winter, 2=Spring, 3=Summer, and 4 = Autumn.
    Add code to return an error message if any other number is entered:
    '''
    '''
    a. 
    '''

    # Check if the an int is specified
    # This part controls the function if the paramater is a int
    if type(number) == int:

        if number in range(85, 101):
                return "A"

        elif number in range(70, 85):
                return "B"

        elif number in range(55, 70):
                return "C"

        elif number in range(40, 55):
                return "D"

        elif number in range(25, 40):
                return "E"

        elif number in range(0 , 5):
                return "F"

        elif number > 100:
            return "The input numerical grade is outside the range supported"

    # This part controls the funtion when the paramater is a string
    if type(number) == str:

        if number == "A":
            return "85-100"

        elif number == "B":
            return "70-84"

        elif number == "C":
            return "55-60"

        elif number == "D":
            return "40-54"

        elif number == "E":
            return "25-39"

        elif number == "F":
            return "0-4"
        else:
            return "The input letter grade is outside the range supported"

    # If type is neither int nor sting return an error
    else:
        return "Input value must be a number or a letter"
