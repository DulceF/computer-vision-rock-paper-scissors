import random

def get_computer_choice():
    
    possible_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(possible_choices)
    return computer_choice

get_computer_choice()

def get_user_choice():
    user_choice = input("What is your choice?: (Rock,Paper or Scissors): ")
    return user_choice
get_user_choice()

import random

user_choice = input("What is your choice?: (Rock,Paper or Scissors)")

possible_choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(possible_choices)

def get_winner(computer_choice, user_choice):

    if computer_choice == user_choice:
        print('It is a tie!')

    elif computer_choice == "Rock":
        if user_choice == "Scissors":
            print("You lost")
        else:
            print("You won!")

    elif computer_choice == "Paper":
        if user_choice == "Rock":
            print("You lost")
        else:
            print("You won!")
        
    elif computer_choice == "Scissors":
        if user_choice == "Paper":
            print("You lost")
        else:
            print("You won!")
   
get_winner(computer_choice, user_choice)

#Task 3 Create a function to simulate the game

#def play(get_computer_choice, get_user_choice, get_winner):

#  play(get_computer_choice, get_user_choice, get_winner)
