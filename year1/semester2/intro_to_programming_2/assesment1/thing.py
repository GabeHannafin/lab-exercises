#Name: Gabriel Hannafin
#Student ID: 121328481
#Programme: CS1117

########################## Question 1 ############################################
def calculate_score (board):

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}

    '''Calculate the score per row and append it to the rowTotals list'''
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
    # return both answers
    return rowTotals, colTotals


def main():
    rTotals, colTotals = calculate_score([["#", "!"],["!!", "X"]])
    print (rTotals, colTotals)
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

if __name__ == "__main__":
    main()
