# ScriptName: main.py
# Author: <add your name here>

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
#    print_function()
    seperated_input("phineas", "ferb", " and ", "rock!!\n")
    seperated_input("doofenshmirtz","incorporated", " Evil ", "!!!\n")
    three_numbers(3,2,3)
    seasons(0)
    grades(89)

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
