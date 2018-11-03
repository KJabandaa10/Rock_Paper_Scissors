#!/bin/python3

from random import randint

player_choice = input("Rock (r), Paper (p) or Scissors (s)?: ")

print(player_choice, end= " vs ")

chosen = randint(1, 3)

win_game = ("You win!")
lose_game = ("You lose!")

if chosen == 1:
  computer_choice = "r"
elif chosen == 2:
  computer_choice = "p"
else:
  computer_choice = "s"

print(computer_choice)

if computer_choice == player_choice:
  print("Draw!")

elif computer_choice == "r" and player_choice == "p":
  print(win_game)
  
elif computer_choice == "r" and player_choice == "s":
  print(lose_game)
  
elif computer_choice == "p" and player_choice == "r":
  print(lose_game)
  
elif computer_choice == "p" and player_choice == "s":
  print(win_game)
  
elif computer_choice == "s" and player_choice == "r":
  print(win_game)

elif computer_choice == "s" and player_choice == "p":
  print(lose_game)
  
