def load_data (filename):

    #create a dictionary - let's call it Infections
    infections = {}

    #read in the data from the file
    with open(filename, "r") as f:
        # use list comprehension to strip all the newlines and spaces and create a nested list
        data = [ line.strip().replace(" ", "").split(",") for line in f ]
        for item in data:
        # convert all the items in data excluding the names of the counties to int
            for i in range(1, len(item)):
                item[i] = int(item[i])
            # Insert all the information into the dict
            infections[item[0]] = item[1:]
    # Return the finished dictionary
    return infections

def daily_cases (cumulative):
    #create a new dictionary called newInfections
    newInfections = {}
    #for every case in the cumulative dictionary i.e. for every county
    for county in cumulative:
        # Add the first number to the dict
        newInfections[county] = cumulative[county][:1]
        #for every item in list of cumulative infection values starting at 1 to exclude the first value
        for item in range(1, len(cumulative[county])):
            # subtract the value before from the current one and store it into a variable
            increase = cumulative[county][item] - cumulative[county][item -1] 
            # Append the increase
            newInfections[county].append(increase)
    #return the newInfections dictionary
    return newInfections

def main():
    cumulativeInfections = load_data("occurences.txt")
    newInfectionRates = daily_cases (cumulativeInfections)
    print(newInfectionRates)


if __name__ == "__main__":
    main()
