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

def meanBoutsAcrossAllPatients(averages):
    # assign the total variable
    total = 0
    # for every average
    for item in averages:
        # add them to the total variable
        total += item
        # calculate the mean without rounding
        mean = total / len(averages)
    # return the total mean
    return mean


def print_averages(averages, all_patients):
    # Print for every patient
    for number in range(len(averages)):
        # print according to the syntax
        print("Patient " + str(number +1 )+ " had " + str(averages[number]) + " inflammatory bouts on average" )
    # print the average for all
    print("The average number of inflammatory bouts on this trial medication is:  " + str(all_patients)) 

def main():
    # get the mean per patient
    mean_per_patient = meanBoutsPerPatient()
    # get the mean for all
    all_patient_mean = meanBoutsAcrossAllPatients(mean_per_patient)
    # print the output
    print_averages(mean_per_patient, all_patient_mean)
    


if __name__ == "__main__":
    main()
