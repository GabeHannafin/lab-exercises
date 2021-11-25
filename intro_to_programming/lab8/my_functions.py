# ScriptName: my_functions.py
# Author: Gabe

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def while_loop(max_number=None):
    """
    while loop that loops from 1 to n, where n is a positive number saving the
    number in a list on each loop
    If no parameter is passed to the function, while_loop()
    shall return the list of numbers from 1 to 10
    """
    # Create an empty list to populate
    le_list = []

    def loop_and_append(length, step=1):
        # Create an interator that starts at 1 not 0 
        i = 1
        accumulator = 0 
        # loop until i is equal to 10
        if step < 0:
            while i >= length:
               # append the value to the list
               le_list.append(i)
               # add every value to the accumulator
               accumulator += i 
               # increment the iterator
               i += step
            # append the accumulator to the end of the list
            le_list.append(accumulator)

        else:
            while i <= length:
                # append the value to the list
                le_list.append(i)
                # add every value to the accumulator
                accumulator += i 
                # increment the iterator
                i += step
            # append the accumulator to the end of the list
            le_list.append(accumulator)


    # if no param supplied
    if max_number == None:
       # call function to create list
       loop_and_append(10)
       # return the finished list
       return le_list 

    elif max_number > 0:
        # call function to create list
        loop_and_append(max_number)
        # return the finished list
        return le_list 

    elif max_number < 0:
        # call function to create list
        loop_and_append(max_number, -1)
        # return the finished list
        return le_list 
        
