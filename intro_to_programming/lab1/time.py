#! /usr/bin/python3

# Script name: time.py
# Author:   Gabe

user_input = int(input("How many minutes did you spend watching TV: "))

hours = user_input//60
remainder = user_input%60

print(f"There were {hours} hours and {remainder} min(s) spent watching TV")



