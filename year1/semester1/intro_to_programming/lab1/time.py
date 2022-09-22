#! /usr/bin/python3

# Script name: time.py
# Author:   Gabe

# Function to get user input
def get_user_input():
    '''function to get user input
    this returns whatever the user supplies as a int'''
    return int(input("How many minutes did you spend watching TV:   "))

def calc(minutes):
    '''
    calculating the hours and minutes spent watching TV
    the function takes the user supplied minutes variable and first devides it by 60 to get the hours
    and then gets the modules to display the minutes left over
    '''
    hours = minutes//60
    remainder = minutes%60
    
    return (hours, remainder)

# Calling function to get the minutes
minutes = get_user_input()

hours, remainder = calc(minutes)

print(f"There were {hours} hours and {remainder} min(s) spent watching TV")



