

import random
score : 0 
def main():
    """Start a music guessing game."""
    print("Lets make our life more hip hop!")
    print ("Your current score is",score)


    music = [
        "pop",
        "jazz",
        "rock",
        "rap"
        ]

    x = random.choice(music)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What music  am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            score=score + 1
            print ("Your current score is",score)
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            print ("Your current score is",score)
main()