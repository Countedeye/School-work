import random
#creates a loop ten times to show "random" outcome.
for i in range(10):
    #list variable.
    outcomes = ["heads", "tails"]
    #variable that stores answer.
    result = random.choice(outcomes)
    print(result)
