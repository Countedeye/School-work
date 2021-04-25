import random

def flip(x,y):
        outcomes = [x,y]
        #variable that stores answer.
        result = random.choice(outcomes)
        print(result)


#calls function "flip".
flip("Husky","Corgi")
