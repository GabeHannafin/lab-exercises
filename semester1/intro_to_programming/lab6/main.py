# ScriptName: main.py
# Author: Gabe

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
    print_function()
    print(seasons(5))
    # Something is broken here with question 2 on rotator
    print(slice_reverse("abcda"))
    print(add_to_list(5,5))
    print(add_to_list_no_sort(5, [3,1,7,9]))
if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
