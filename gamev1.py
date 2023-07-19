import random

print("...rock...")
print("...paper...")
print("...scissors...")

print(random.randint(1,3))

player1Choice = input("Enter player1's choice ")
player2Choice = input("Enter player2's choice ")

if player1Choice and player2Choice:
    if player1Choice == player2Choice:
        print("It's a draw!") 
    elif player1Choice == "rock" and player2Choice == "paper":
        print("Player2 wins")
    elif player1Choice == "rock" and player2Choice == "scissors":
        print("Player1 wins")
    elif player1Choice == "paper" and player2Choice == "rock":
        print("Player1 wins")
    elif player1Choice == "paper" and player2Choice == "scissors":
        print("Player2 winds")
    elif player1Choice == "scissors" and player2Choice == "rock":
        print("Player2 wins")
    elif player1Choice == "scissors" and player2Choice == "paper":
        print("Player1 wins")
else:
    print("Missing values")