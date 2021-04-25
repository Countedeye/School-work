import random


def flip(x, y):
    outcomes = [x, y]
    #variable that stores answer.
    result = random.choice(outcomes)
    print(f"The coin landed on {result}")
    return result


guess = input("Guess the result. Type either \"heads\" or \"tails\" and press ENTER:\n> ")
guess = guess.strip().lower()
flipResult = flip("HEADS","TAILS")
flipResult = flipResult.strip().lower()
if guess == flipResult:
    print("You win!")
else:
    print("Sorry you lose...")