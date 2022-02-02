def dna_to_list():
    """
    Function to grab and split the data from the file then
    strip the trailing newline characters and add it to a
    finished list
    """ 
    
    # open the file using with so we don't have to close it
    with open("dna.txt", "r") as InFile:
        # Split the file on double newlines
        RawFile = InFile.read().split("\n\n")
        # strip the trailing newlines and add to finished list
        DnaList = [item.replace("\n", "") for item in RawFile ]
        # return the finished list
        return DnaList
        
def print_dna(rawlist):
    """
    Function to take the list from before and print it out
    to the specified format
    """
    # grab the index and item from every item in the list
    for index,item in enumerate(rawlist):
        # print to the given standard
        print(str(index) + " : " + str(item), end="\n\n")

# run the code
def main():
    print_dna(dna_to_list())


if __name__ == "__main__":
    main()
