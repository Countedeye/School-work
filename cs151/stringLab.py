# William Sutton
# cs15120

import random

# function that searches a list and returns whether the word exists in the list or not.
def foundCode(word,codeList):
    flag = False
    for val in codeList:
        if str(val) == word:
            flag = True
    return flag        


# function that splits white space between words and creates a list of all words in sentence.
def wordCount(phrase):
    sentence = phrase.split()
    for val in phrase:  
        sentence == []
    return sentence

# function that changes characters to symbols.
def hideIt(code):
    myChars = ['#','@','!','*','%']
    newCode = ""
    for chars in code:   
        newCode += myChars[random.randint(0,4)]
    return newCode

# function that creates each letter of word to unicode, then adds five to value to change cipher.
def cipherIt(word,number):
    uniWord = ""
    for i in range(len(word)):
        # removes "-" from beginning of output.
        if i == 0:
            uniWord = uniWord + str(ord(word[i])+number)
        else:
            uniWord = uniWord + "-" + str(ord(word[i])+number)
    return uniWord

# function that deciphers unicode.
def decipherIt(phrase,number):
    uniWord = ""
    #identifies each letter by splitting between dash.
    newList = phrase.split("-")
    # searches each unicode and converts back to character.
    for i in newList:  
        uniWord = uniWord + chr(int(i)-number)
    return uniWord    



#example list for foundCode function.
codeList=['Nalla', 'Kota', 'Sylvi', 'cat', 'dog', 'weather', 'green']
#examples of receiving true or false boolean values for foundCode function.
print(foundCode('Nalla', codeList))
print(foundCode('blue', codeList))

#example sentence for wordCount function.
phrase = "This is a helpful assignment on strings."
#printed out example as a list.
print(wordCount(phrase))

#example sentece for hideIt function.
example = "this works."
print(hideIt(example))

#example for cipherIt function.
example = "dog"
#example for original cipher text and added 5.
print(cipherIt(example,0))
myVar = (cipherIt(example,5))
print(myVar)

#example for decipher function (extra credit). uses code from cipher it function.
print(decipherIt(myVar,5))
