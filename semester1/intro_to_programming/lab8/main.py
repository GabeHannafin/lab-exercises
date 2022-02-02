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
    # print_function()
    print(while_loop((False)))
    # 8 ball testing
    print(magic_8_ball("Why is your hair long?", [200]))
    print(magic_8_ball("Why is your hair long?"))
    print(magic_8_ball("Why is your hair long?", [1, 1]))
    print(magic_8_ball("Why is your hair long?", [1, 1]))
    print(magic_8_ball("Why is your hair long?", [1, 1]))

    # stairs testing
    print(is_stairs([2,3,4,5]))
    print(is_stairs([2,3,2]))
    print(is_stairs([4]))
    print(is_stairs([]))

    print(is_stairs(["a", "b", "c"]))
    print(is_stairs(["c", "b", "a"]))
    print(is_stairs(["a", "B", "c"]))
    print(is_stairs(["a", "b", "C"]))
    print(is_stairs(["c", "B", "a"]))
    print(is_stairs(["C", "b", "a"]))


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
