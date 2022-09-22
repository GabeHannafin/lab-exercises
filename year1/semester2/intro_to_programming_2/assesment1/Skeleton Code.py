#Name: Gabriel Hannafin
#Student ID: 121328481
#Programme: CS1117

########################## Question 1 ############################################
def calculate_score (board):

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}

    '''Calculate the score per row and append it to the rowTotals list'''
    '''
    The first loop controls iterating through the rows and the second iterates through each item contained there
    '''
    # Initialise the rowTotals List
    rowTotals = []
    # for every row in the matrix
    for row in board:
        # reset the sum variable for every new row 
        sum = 0
        # for every value in the row
        for item in row:
            # lookup each item in the row in the symbols dictionary and add the associated value to the sum variable
            sum += symbols[item]
        # if the sum is negative set sum to 0
        if sum < 0:
          sum = 0
        # append the sum of each row to the rowTotals list
        rowTotals.append(sum)

    '''Calculate the score per column and append it to the colTotals list'''
    # Initialise the list to contain the totals for the column sum
    colTotals = []
    '''
    since the amount of rows dictates the amount of items in each column, the length of the board list
    is equal to the amount of items in each column
    '''
    # for every item in the column
    for length in range(len(board)):
        # reset the sum variable after each column
        sum =0
        # Iterate through each column in the matrix 
        for row in board:
            # look every item in the column up in the symbols dictionary and add the associated value to the sum variable
            sum += symbols[row[length]]
        # if the sum is negative set sum to 0
        if sum < 0:
            sum =0
        # append the sum for each column to the colTotals list
        colTotals.append(sum)
    # return both the answers
    return rowTotals, colTotals

rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])
print (rTotals, cTotals)

########################## Question 2 ############################################
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

print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0
