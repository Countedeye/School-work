import random
   
# increments count of either heads or tails on each toss
def incrementHeadTails(coinList):
    numHeads = 0
    numTails = 0
    for i in coinList:
        if i == 1:
            numHeads += 1
        elif i == 2:
           numTails += 1
    print("Number of heads: " + str(numHeads))
    print("Number of tails: " + str(numTails))


#creates the list of heads and tails 
def appendCoinList(coinList):
    # Code that creates a list of 10000 'heads' or 'tails' values.
    for i in range(10000):
        #This creates the random flip generation
        coinFlip = random.randint(1, 2)
        coinList.append(coinFlip)

#function that counts the longest streak after running for loop.
def findLongestStreak(coinList):
    longestStreak = 0
    numHeads = 0
    numTails = 0
    for i in coinList:
        if i == 1:
            numHeads += 1
            if numTails > longestStreak:
                longestStreak = numTails
            numTails = 0
        elif i == 2:    
            numTails += 1
            if numHeads > longestStreak:
                longestStreak = numHeads
            numHeads = 0
    print('Longest streak: ' + str(longestStreak))

# This creates a streak list (added likely not working.)
def countNumberStreaks(coinList):
    myStreak = 0
    numHeads = 0
    numTails = 0
    for i in coinList:
        if i == 1:
            numHeads += 1
            if numTails >= 6:
                ++myStreak
            numTails = 0
        elif i == 2:
            numTails += 1
            if numHeads >= 6:
                ++myStreak
            numHeads = 0
    print('number of streaks >= 6: ' + str(myStreak))

#creates list
coinList=[]

# calling each function
appendCoinList(coinList)
findLongestStreak(coinList)
countNumberStreaks(coinList)
incrementHeadTails(coinList)


