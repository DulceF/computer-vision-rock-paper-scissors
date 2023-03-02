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
       print("It is a tie!")

#1
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print("You won")
        else:
            print(" You lost")

#2
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("You won")
        else:
            print("You lost")
 #3   
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print("You won")
        else:
            print("You lost")

   

get_winner(computer_choice, user_choice)

#Task 3 Create a function to simulate the game

def play(get_computer_choice, get_user_choice, get_winner):

    play(get_computer_choice, get_user_choice, get_winner)
