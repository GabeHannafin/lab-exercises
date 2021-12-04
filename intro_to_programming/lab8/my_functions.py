# ScriptName: my_functions.py
# Author: Gabe

import random


# template for calling functions in another file
def print_function():
    print("I'm in another file :)")


def while_loop(max_number: int=None):
    """
    while loop that loops from 1 to n, where n is a positive number saving the
    number in a list on each loop
    If no parameter is passed to the function, while_loop()
    shall return the list of numbers from 1 to 10
    """
    # Create an empty list to populate
    finished_list = []

    def loop_and_append(length: int, step: int =1):
        # Create an interator that starts at 1 not 0 
        i = 1
        accumulator = 0 
        # loop until i is equal to 10
        if step < 0:
            while i >= length:
               # append the value to the list
               finished_list.append(i)
               # add every value to the accumulator
               accumulator += i 
               # increment the iterator
               i += step
               # stop counting if i is -12 
               if i < -12:
                    # break the loop
                    break
                # append the accumulator to the end of the list
            finished_list.append(accumulator)
            

        else:
            while i <= length:
                # append the value to the list
                finished_list.append(i)
                # add every value to the accumulator
                accumulator += i 
                # increment the iterator
                i += step
                # append the accumulator to the end of the list
                # stop counting if i is 12 
                if i > 12:
                    # break the loop
                    break
            finished_list.append(accumulator)

    try:
            # if no param supplied
        if max_number == None:
           # call function to create list
           loop_and_append(10)
           # return the finished list
           return finished_list 

        elif max_number > 0:
            # call function to create list
            loop_and_append(max_number)
            # return the finished list
            return finished_list 

        elif max_number < 0:
            # call function to create list
            loop_and_append(max_number, -1)
            # return the finished list
            return finished_list 

    except Exception: 
        return "Did you break the break or should we continue?"

def magic_8_ball(my_question, fixed_list=[]):
    # Creation of altered list
    altered_list = []
    # List containing all the possible answers
    silly_answers = [
    
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
    ]


    try:
        # if fixed_list contains -1
        if -1 in fixed_list:
            # Throw a type error
            try:
                1 / "Cheese"
            ## Except it
            except TypeError as e:
                # return the error
                return str(e)
        # If fixed_list is not default
        elif len(fixed_list) > 0:
            # for every item in silly_items
            for x in silly_answers:
                # If the index of of every item in silly_answers is equal to the indexes in fixed_list
                if silly_answers.index(x) in fixed_list:
                    # Append the items to altered_list
                    altered_list.append(silly_answers[silly_answers.index(x)])
            # Generate a random number the length of fixed_list
            random_number = random.randint(0, len(altered_list)-1)
            # Return random from the altered_list
            return altered_list[random_number] 

        elif len(fixed_list) == 0:
            # Generate a random number within the range of the list
            random_number = random.randint(0, len(silly_answers)-1)
            # return a random list item
            return silly_answers[random_number]

    except Exception:
        return "I have spoken."

def is_stairs(s=[0]):

    try:
        # A one length list is not a stairs by default
        if len(s) > 1:
            # This is for checking if a list of ints is a stairs
            if type(s[0]) == int:
                # if the first number is a stairs in ascending order
                if s[1] == s[0]+1:
                    # for every item in s
                    for x in s:
                        # If the index of x is equal to the length it means that it has iterated the full list
                        if s.index(x) == len(s)-1:
                            # break the loop
                            break
                        # Continue until x doesnt equal (x-1)+1
                        if x != s[s.index(x)+1]-1:
                            return False
                    # If the loop completes without returning False then it has successfully iterated through all the items
                    return True

                # mostly the same just for the reverse stairs
                elif s[1] == s[0]-1:
                        # for every item in s
                        for x in s:
                            # If the index of x is equal to the length it means that it has iterated the full list
                            if s.index(x) == len(s)-1:
                                # break the loop
                                break
                            # Continue until x doesnt equal (x-1)-1
                            if x != s[s.index(x)+1] +1:
                                return False
                    # If the loop completes without returning False then it has successfully iterated through all the items
                        return True
                # If the first number is not a stairs return False
                else:
                    return False
            
            # Very similar code for strings, comparing the ord values against each other to compare position in the alphabet
            if type(s[0]) == str:
                # An uppercase letter has a different ord value to a lowercase therefore we convert all the strings to lowercase
                if ord(s[1].lower()) == ord(s[0].lower())+1:
                    # For every item in s
                    for x in s:
                        # If the index of x is equal to the length it means that it has iterated the full list
                        if s.index(x) == len(s)-1:
                            # break the loop
                            break
                        # Same as the code above, if the ord value of x is not equal to the ord value of the next index -1 
                        if ord(x.lower()) != ord(s[s.index(x)+1].lower())-1:
                            # return False
                            return False

                    # If it completes the loop then it has succesfully iterated through all the items
                    return True

            # Same as before just for descending stairs
                elif ord(s[1].lower()) == ord(s[0].lower())-1:
                    # For every item in s
                    for x in s:
                        # If the index of x is equal to the length it means that it has iterated the full list
                        if s.index(x) == len(s)-1:
                            # break the loop
                            break
                            # Same as the code above, if the ord value of x is not equal to the ord value of the next index +1 
                        if ord(x.lower()) != ord(s[s.index(x)+1].lower())+1:
                            # Return False
                            return False

                    # If it completes the loop then it has succesfully iterated through all the items
                    return True
                # If the first 2 indexes are not stairs
                else:
                    return False

        # Return False if the length of s is 1
        else:
            return False

    # General error handling
    except Exception:
        return "How can I get to the second floor if I do not have a stairs?"
