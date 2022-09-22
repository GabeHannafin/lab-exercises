#! /usr/bin/python3


import random

# Get the amount of students we are getting the average of
def number_of_students():
    try:
        return int(input("Good 'een Sirrah, how many grace us today?: "))
# Error Handling
    except ValueError:
        print("\nThat's not a number, don't be a bitch\n")               # error handling for non int input
        exit(0)
    except KeyboardInterrupt:
        print("\nAAAAAAAAAAAAAAAAAAAAAAHHHH")
        exit(0)
        

# function to get age input
def get_age(string_to_print):
    try:
        return int(input(string_to_print))

    except :
        print("That's not a number, don't be a bitch\n")               # error handling for non int input
        exit(0)
    

    
# function to calculate the average
def get_average(sum_of_ages):
    return int((sum_of_ages)/amount)


# variables to control iteration
amount = number_of_students()
times_asked = 1
sum_of_ages = 0

prompts = ["V'ry valorous sir, anoth'r?", "One more?", "Thanketh thee, prithee continueth", "My Lord is too kind"]

# getting the ages using the function
while times_asked <= amount:
    chosen_prompt = random.choice(prompts)

    if times_asked == 1:
        sum_of_ages += get_age("Prithee, What is thine first age?: " )
        times_asked += 1
    try:
        sum_of_ages += get_age(chosen_prompt + ": ")
        times_asked += 1
    
    except ValueError:
        print("That's not a number, don't be a bitch")
    except KeyboardInterrupt:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAHH")
        exit(0)    


# saving the result as a variable
result = get_average(sum_of_ages)

# printing the result
print (f"Thine average age is {result}")
