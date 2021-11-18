# ScriptName: my_functions.py
# Author: Gabe

# template for calling functions in another file

def print_function():
    print("I'm in another file :)")

def list_to_string(my_list):
    # Set Counter
    i = 0
    # declare the finished_string variable
    finished_string = ""
    # Loop through every element in my_list
    while i < len(my_list):
    # add the values to the finished string
        finished_string += my_list[i]
    # increment the iterator
        i += 1
    # return the finished string
    return finished_string


def count(my_list, value):
    '''
    function - count how many times <value> occurs in <my_list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return:
    '''
    # set counter
    i = 0
    # accumulator to count how many times <value> occurs
    # set to zero to cover no <value> in <list>
    num_values = 0
    # Try
    try:
        # loop over the length of the <list>
        while i < len(my_list):
            # if <value> and <list> index i are the same
            if my_list[i] == value:
                # increment the accumulator
                num_values += 1
            # increment the counter
            i += 1
        # return how many times <value> occurs in <list>
        return num_values

    # If there is an error
    except Exception:
    # return the error message
        return "Houston, we have a problem!"

def index(my_list, value):
    """
    Function to return the first index that value occurs in my_list
    return -1 if the value does not occur in my_list
    """
    # Set Counter
    i = 0
    # Try
    try:
        # Loop over the length of my_list
        while i < len(my_list):
        # if <value> is equal to the value at index i, return i
            if my_list[i] == value:
                return i 
        # if <value> is not present in my_list return -1
            if value not in my_list:
                return -1
        # increment the iterator
            i += 1

    # If there is an error
    except Exception:
    # return the error message
        return "Houston, we have a problem!"

def get_value(my_list=[], index=0):
    """
    Function to return the value that occurs in <list> at index.
    If index does not return a valid value from my_list, it should
    return the error message"Houston, we have a problem!"
   """ 
    # Set Counter
    i = 0

    # Try
    try:
        # Loop over the length of my_list
        while i < len(my_list):
        # return the value that is at index <index>
            return my_list[index]
        # increment the iterator
            i += 1

    # if <index> is not a valid index return an error message
    except Exception:
        return "Houston, we have a problem!"


def insert(my_list=[], index=0, value="a"):
    """
    Function to return my_list, after you have added value at <index> index
    remember to check the length of my_list and if index is larger than the length
    add as a new index at the end
    """
    # Cast my_list to type list
    my_list = list(my_list)

    try:
        # if the index param is larger than len <list> just append it
        if index >= len(my_list):
        # append <value> to the end of <list>
            my_list.append(value)
        # format the list to a string
            return(list_to_string(my_list))

        # else if the value is not larger than the len of my_list    
        else:
        # substitute the value at i for the value supplied
            my_list[index] = value
        # format the list to a string
            return(list_to_string(my_list))

    # if <index> is not a valid index return an error message
    except Exception:
    # return error message
        return "Houston, we have a problem!"

def value_in_list(my_list=[], value=""):
    # Set counter
    i = 0

    try:
        # Loop through every element in my_list
        while i < len(my_list):
        # If the value is equal to value at list index i
            if value == my_list[i]:
        # return True
                return True
        # if the loop has iterated throughtout the whole list without finding <value>
            elif i == len(my_list)-1:
        # return False
                return False
        # Increment the interator
            i +=1

    # if <index> is not a valid index return an error message
    except Exception:
    # return error message
        return "Houston, we have a problem!"


def concat(list1, list2):
    # convert string input to a list
    list1 = list(list1)
    list2 = list(list2)

    # Set counter
    i = 0

    try:
        # Loop to the length of list2
        while i < len(list2):
        # Append the entire contents of list2 to the end of list1
            list1.append(list2[i])
        # Increment the iterator
            i +=1
        # Return the formatted result
        return list_to_string(list1)

    # if <index> is not a valid index return an error message
    except Exception:
    # return error message
        return "Houston, we have a problem!"


def remove(value="", my_list=[]):
    # Created the list we will return
    edited_list = []

    # Set counter
    i = 0

    try:
        # Loop through the contents of my_list
        while i < len(my_list):
        # if the value is not equal to the value at index i then append it to the new list
            if my_list[i] != value:
                edited_list.append(my_list[i])
        # if the value is equal to the value at index i then pass
            elif my_list[i] == value:
                pass
        # Increment the Iterator
            i += 1
        # Return the formatted string
        return list_to_string(edited_list)
            
    # if <index> is not a valid index return an error message
    except Exception:
    # return error message
        return "Houston, we have a problem!"
