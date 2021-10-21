#! /usr/bin/python3

# Script Name: rugby_matches.py
# Author: Gabe

# Pseudocode
'''
Prompt 'Enter the name of team 1:' and store in team1
• Prompt 'Enter the name of team 2:' and store in team2 
• Prompt 'Enter the number of tries for ' + team1 and store in tries_for_team1
• Prompt 'Enter the number of tries for ' + team2 and store in tries_for_team2
• Prompt 'Enter the number of converted/penalty for' + team1 and store in points
_team1
• Prompt 'Enter the number of converted/penalty for' + team2 and store in points
_team2
• Print the results headings
• print team1 + tab + tries_for_team1 + tab + points_team1
• print team2 + tab + tries_for_team2 + tab + points_team2
• try to use string formatting as well as tab to align the formatting
'''

def rugby1():
    team1 = input("What is the name of the first team?: ")
    team2 = input("What is the name of the second team?: ")

    tries_for_team_1 = input(f"Enter the number of tries for {team1}:   ")
    tries_for_team_2 = input(f"Enter the number of tries for {team2}:   ")

    points_team1 = input(f"Enter the number of converted/penalty for {team1}:    ")
    points_team2 = input(f"Enter the number of converted/penalty for {team2}:    ")


    print("\tResults\t", "Team\tTries\tPoints", "-"*23, sep="\n")
    print(f"{team1}\t{tries_for_team_1}\t{points_team1}", sep="\n")
    print(f"{team2}\t{tries_for_team_2}\t{points_team2}", sep="\n")

# Pseudocode
'''
• Prompt ‘Rugby Players Name: ’ 
• Save rugby_name
• Prompt ‘Enter no. of days old: ’
• Save days_old
• Calculate no_of_years
• Calculate remaining_days
• Print rugby_name + ‘ is ‘ + no_of_years + ‘ years and ‘ + remaining_days + 'days
old.'
'''
def ages():
    rugby_name = input("Rugby Player's name?: ") 
    days_old = int(input("Enter n. of days old: "))

    no_of_years = str(days_old // 365)
    remaining_days = str(days_old % 365)

    print(rugby_name  + " is " + no_of_years + " years and " + remaining_days + " days old."  )

def calc_seconds():
    mins = 42
    seconds = 42
    answer = (mins * 60) + seconds
    print(f"There are {answer} seconds in {mins} minutes and {seconds} seconds")


def calc_miles():
    kilometres = 10
    answer = kilometres / 1.61
    print(f"There are {answer:.2f} miles in {kilometres}km")

def calc_pace():
    km_distance = 10
    miles_distance = km_distance / 1.61
    mins = 42
    seconds = 42
    time_in_seconds = (mins * 60) + seconds

    pace = (time_in_seconds / miles_distance) / 60
    average_speed = (miles_distance / time_in_seconds) * 60

    print(f"On average it took {pace:.2f} minutes to complete one mile.")
    print(f"The average speed was {average_speed:.2f} miles per minute")


if __name__ == "__main__":
    ages()
    calc_seconds()
    calc_miles()
    calc_pace()
    
