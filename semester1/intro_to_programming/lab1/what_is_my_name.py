#! /usr/bin/python3

# Scipt name:   what_is_my_name
# Author:   Gabe


'''
Ask "whats th first name " and store as a variable
ask "whats the second" and store as a variable
display the two names concat together
'''
# Function to get the user's name
def get_user_input():
    first_name = input("Fuck you, what's your first name?: ")
    second_name = input("Fuck you, what's your second name?: ")
    return (first_name, second_name)

# Calling the function and assigning it    
first_name_output, second_name_output = get_user_input()

print("Fuck you", first_name_output, second_name_output)
