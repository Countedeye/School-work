
def headOfFile(myFile):
    lineNum = 0
    for x in range(5):
        print(myFile.readline())

def tailOfFile(myFile):
   lineNum = 0
   lines = myFile.readlines()
   for line in reversed(lines):
        if lineNum < 5:
            print(line)
        lineNum += 1    

def wc(myFile):
    stringFile = myFile.read()
    wordCount = stringFile.split()
    lineCount = stringFile.splitlines()
    print(f"Line Count = {len(lineCount)}")
    print(f"word count = {len(wordCount)}")



def stats(myFile):
    fileString = myFile.read()
    words = fileString.split()
    maxNum = int(words[0])
    minNum = int(words[0])
    avg = 0
    numberCount = 0 
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
#myFile = open("/Users/william.sutton/Desktop/School work /School-work/cs151/number.txt", "rt")
myFile = open("textFile.txt", "rt")

#Calling each function.
headOfFile(myFile)
tailOfFile(myFile)
wc(myFile)
stats(myFile)
