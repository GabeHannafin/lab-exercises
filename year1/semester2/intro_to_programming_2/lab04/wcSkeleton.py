def readFile (filename):
    with open ("books.txt", "r") as book:
        words = []
        raw = book.read()
        cleaned = raw.strip().replace("-", " ").split()

        for item in cleaned:
            words.append(item.lower())
        return words


def depunctuate (words):
    punctuation = [",", ".", "!", "?", "-", "'", '“', '”', "–", ';']
    cleaned_words = []
    for item in words:
        for char in punctuation:
            if char in item:
                item = item.replace(str(char), "")
        cleaned_words.append(item)

    # return text
    return cleaned_words

def countWords (words):
    #create a dictionary
    wc = {}
    #if a word doesn't exist add it as a key with 1 as a value
    for word in words:
        if word not in wc:
            wc[word] = 1
        #if it does exist add 1 to the current count
        else:
            wc[word] = wc[word] +1
    highest = 0
    #process the dictionary to see which word has the highest count.
    for item in wc.values():
         if item > highest:
             highest = item

    #write this to an output file
    with open("output.txt", "w") as outFile:
        outFile.write(str(highest))

#Main Program:

#read in the file to get a list of words (best use a function)
# words_text = print(readFile("books.txt"))
words_text = readFile("books.txt")

#depunctuate the lists of words
words_cleaned = depunctuate(words_text)

#count the words, calculate the max and write to a file
print(countWords(words_cleaned))
