# William Sutton
# cs15120



# parses the string passed in as "phrase" by the character "charact" and returns the resulting list.
# Asks the user for a phrase. Then asks the user to remove characters. 
# outputs sentence without chosen characters.
def splitIt(phrase,charact):
    userStr = ""
    # removes the letter the user chooses.
    userList = phrase.split(charact)
    for i in range(len(userList)):
        if userList[i] == charact:
            userList[i] = [ ]
        userStr = userStr + userList[i]    
    return  userStr   


# This function returns "True" if the word is a palindrome, 
# otherwise returns "False"
def palindrome(word):
    revWord = ""
    #begins reading from the end of the word to the beginning.
    for i in range (len(word)-1, -1, -1):
        revWord = revWord + word[i]
    if revWord == word:
        return True
    else:
        return False


#converts the word to its Unicode values, separated by "-" so "dog" is "100-111-103". This new string is returned.    
# returns uniWord as a string.
def changeToNumber(word):
    uniWord = ""
    for i in range (len(word)):
        # removes "-" from beginning of output.
        if i == 0:
            uniWord = uniWord +  str(ord(word[i]))
        else:
            uniWord = uniWord + "-" + str(ord(word[i]))       
    return uniWord 


#outputs functions and main code for splitIT.
phrase = input("Please write a phase that can be manipulated by character: ")
charact = input("Now please take a letter away from your phrase: ")
split = splitIt(phrase,charact)
print(split)

#outputs functions and main code for palindrome.
word = input("Please write a word to find out if it is a palendrome: ")
boolean = palindrome(word)
print(word + " is " + str(boolean))

#outputs functions and main code for changeToNumber.
word = input("Please write a word to change into Unicode. ")
chngeNum = changeToNumber(word)
print(chngeNum)
