#Task 1 - Store the user's and the computer's choices
#import random
#possible_choices = ["rock", "paper", "scissors"]
import random

def get_computer_choice():
    
    possible_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(possible_choices)
    return computer_choice

get_computer_choice()

def get_user_choice():
    user_choice = input("What is your choice?: (rock,paper or scissors): ")
    return user_choice
get_user_choice()

#Task 2 - Figure out who won
# I win if r>s, p>r, s>p

user_choice = input("What is your choice?: (rock,paper or scissors) ")
possible_choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(possible_choices)

def get_winner(computer_choice, user_choice):
     
    if computer_choice == user_choice:
            return "It is a tie" 

    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            return "You won"
        else:
            return "You lost"

    elif computer_choice == "Rock":
        if user_choice == "Paper":
           return "You won"
        else:
            return "You lost"
   
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            return "You won"
        else:
            return "You lost"
   
get_winner(computer_choice, user_choice)

#Task 3 Create a function to simulate the game

#def play(get_computer_choice, get_user_choice, get_winner):

#  play(get_computer_choice, get_user_choice, get_winner)
