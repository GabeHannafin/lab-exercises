# ScriptName: my_functions.py
# Author: Gabe

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")

def seasons(number):
    """
    I want you to rewrite the seasons() function from Lab 4. Within this
    function, define a list of the seasons, and select the season based on the
    input value where 1=Winter, 2=Spring, 3=Summer, and 4=Autumn. Remember list
    indexing begins at 0. All other error message handling, param names, etc.,
    in the original function, must be kept.
    """
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    
    if type(number) != int:    
        return "Input value must be a number"

    elif number > 4 or number < 1:
     return "Number entered " + str(number) + " is outside of input values"

    else:
        return seasons[number -1]

def slice_reverse(input_value):
    """
    This question examines string slicing. Write a function,
    slice_reverse(input_value), which determine if the input_value is a
    palindrome i.e. reads the same backwards as forwards. The program should
    return True or False (booleans) depending on the input. Do not use the
    Python reverse() function
    """ 
    input_value = str(input_value)

    if (input_value == input_value[::-1]):
        return True
    else:
        return False

def add_to_list(value="", list=[]):
    """
    I want you to create a function called add_to_list(value, list), which will
    return a sorted list. This function will add value to the list if the list
    does not already contain the value. For now, you can assume the list param
    is already sorted. You can use the python function “sort()” to sort your
    returning list. Sort() will not allow you to mix ints, floats and strings.
    In your function set an appropriate default value for the list param.
    Examples:
    """
    # add the value to the list if it is the correct type
    try:
        list.append(value)

    except Exception:
        return "Incorrect value defined for param list"
    # attempt to sort the list, or return an error 
    try:
        list.sort()

    except TypeError:
        return "sort() does not like this mixture of elements"

    return list
   
def add_to_list_no_sort(value, list):
    '''
    it may look as if i have not put any time into this and didn't get it done
    but i most definitely spent hours and hours trying to make this work, alas
    i'm a dumbass
'''
    return
#    i = 0
#    sorted_list = []
#    list.append(value)
#
#
#    while list:
#        if i == (len(list)):
#            i = 0
#            sorted_list.append(list[0])
#            list.remove(list[0])
#        elif list[i] < list[0]:
#            sorted_list.append(list[i])
#            list.remove(list[i])
#        
#        i += 1 
#        
#
#    return sorted_list, list, i

#    while j < len(list):
#        print(i)
#        if i == (len(list)-1):
#            i = 0
#            j += 1
#
#        if list[i] < list[j]:
#            org_list.insert(0, list[i])
#            del list[0]
#
#        i += 1
