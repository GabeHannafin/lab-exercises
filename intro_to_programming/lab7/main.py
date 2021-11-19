# Author: Gabe

# template for calling functions in another file

# import functions from other files - different options
# from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()

    # test count
    # print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 4))
    # print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 8))
    # print(count("hello", "l"))
    # print(count("hello", "h"))
    # print(count("name", "a"))

    # test index
    # print(index("name", "i"))
    # print(index("hello", "p"))

    # test get_value
    # print(get_value([], 1))

    ## test insert
    # print(insert(454545454, 4, "t"))

    ## test value_in_list
    # print(value_in_list(5.6, "t"))

    ## test concat
    # print(concat(("sydney", "gabe"), ("fuck", "shit")))

    ##test remove
    print(remove(7.4, 7.4))


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
