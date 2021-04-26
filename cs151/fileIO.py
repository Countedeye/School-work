# William Sutton
# cs15120

def headOfFile(myFile):
    #searches through file from beginning line in an increment of 5.
    for x in range(5):
        print(myFile.readline())

def tailOfFile(myFile):
   lineNum = 0
   #searches the file in reverse by increment of 5.
   for line in reversed(myFile.readlines()):
        if lineNum < 5:
            print(line)
        lineNum += 1    

def wc(myFile):
    stringFile = myFile.read()
    #creates array of words by spitting on whitespace.
    wordCount = stringFile.split()
    #creates array of lines by splitting on whitepspace.
    lineCount = stringFile.splitlines()
    #prints variables.
    print(f"Line Count = {len(lineCount)}")
    print(f"word count = {len(wordCount)}")



def stats(myFile):
    fileString = myFile.read()
    #creates array of words by splitting on whitespace.
    words = fileString.split()
    #variables that hold maximum and minimum number.
    maxNum = int(words[0])
    minNum = int(words[0])
    #variable that holds average and number count.
    avg = 0
    numberCount = 0 
    #for loop that searches for highest and lowest number. Also searches for avg.
    for word in words:
        numberCount += 1
        
        if int(word) > int(maxNum):
            maxNum = word
        elif int(word) < int(minNum):
            minNum = word  
        avg = avg + int(word)
    avg = avg / numberCount
    print(f" Maximum: {maxNum}")
    print(f" Minimum: {minNum}")
    print(f" Average: {avg}")


# user will need to import files from their own computer. This is my imported domain. to write the code and check.
myFile = open("number.txt", "rt")
#myFile = open("textFile.txt", "r")

#Calling each function.
headOfFile(myFile)
tailOfFile(myFile)
myFile.close()
#I needed to close the file and reopen to get the word count to count correctly.
myFile = open("number.txt", "rt")
wc(myFile)

file2= open("number.txt","r")
stats(file2)
