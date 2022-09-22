def identifyPivot (L):
    '''
    Iterates through all the numbers in the list, adding the numbers that follow it 
    together and then adding the numbers before it  and comparing the two
    '''
    # Initialise pivot variable and set the default to -1
    pivot = -1
    # Initialise both variables for the totals
    totalBefore = 0
    totalAfter = 0
    '''
    enumerate is used here istead of just a plain for loop to deal with a list
    that contains repeated values. the index of the current number is required
    in order to add all the numbers that come after. If you dont use enumerate
    and use the index() function on the list it will only return the index of 
    the first occurance of that number.
    '''
    # for every singe number in the list
    for index, number in enumerate(L):
        # reset the total after the number for every number
        totalAfter = 0
        # Iterate from the number after your current number to the end of the list
        for i in range(index +1, len(L)):
            # Add all the following numbers together
            totalAfter += L[i]
        # if the totals on each side of the number are equal
        if totalAfter == totalBefore:
            # then the pivot has been found
            pivot = number
        else:
            # if they are not equal then add the current number to the totalBefore before moving on
            totalBefore += number
    # return the pivot ( since pivot is initialised as -1 if the totals are never equal then -1 is returned )
    return pivot


def main():
    print(identifyPivot([9,1,9])) #returns 1
    print(identifyPivot ([8,8,8,8])) #returns -1
    print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
    print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0


if __name__ == "__main__":
    main()
