import random


def flip():
    outcome1 = ["love", "hate"]
    outcome2 = ["honda","Ford"]
    #variable that stores answer.
    result1 = random.choice(outcome1)
    result2 = random.choice(outcome2)
    print(f"I {result1} {result2}! ")


#calls function "flip".
flip()
flip()
flip()