import random

playing = True

while playing:
    roundNotFinished = True
    print("Welcome to the game. Guess what number I am thinking of")
    randomInt = random.randint(1,10)

    while roundNotFinished:
        userIn = input("What is your guess?")
        userIn = int(userIn)
        if userIn == randomInt:
            print("You guessed correctly, well done!")
            roundNotFinished = False
        elif userIn < randomInt:
            print("Too low!")
        else:
            print("Too high!")
    
    userIn = input("Want to play again (y/n)?")
    if userIn == "n":
        playing = False
        print("Thanks for playing \U0001f600")
