#! /usr/bin/env python3

def meanBoutsPerPatient():
    """
    Function to calculate the average bouts per person
    """
    # Open the data file
    with open("InflammatoryIBS.csv", "r") as InFile:
        # create a list holding all the information
        data = [ line.strip().split(",") for line in InFile ]

    # assign the total variable
    total = 0
    # create an empty list for the averages
    averages = []
    # for every person in the list
    for item in data:
        # for all the data on that person
        for number in item:
            # add each number to the total
            total += int(number)
            # divide by the amount of data to get the mean
            mean = total // len(item)
        # reset total for the next person
        total = 0
        # append the average to the list
        averages.append(mean)
    # return the finished list
    return averages

