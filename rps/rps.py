from random import choice

player1Choice = input("Player 1: Choose beetween rock, scissors & paper")
player2Choice = input("Player 2: Choose beetween rock, scissors & paper")

if player1Choice == "rock" and player2Choice == "scissors":
  print("Player1 wins!")
elif player1Choice == "rock" and player2Choice == "paper":