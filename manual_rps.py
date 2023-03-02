#Task 1 - Store the user's and the computer's choices
#import random
#possible_choices = ["rock", "paper", "scissors"]
import random

def get_computer_choice():
    
    possible_choices = ["rock", "paper", "scissors"]
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
possible_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choices)

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
       print("Both players have chosen {user_choice}. It is a tie!")

#1
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors, you won!")
        else:
            print("Paper covers rock, You lost!")

#2
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock, You won!")
        else:
            print("Rock smashes scissors, You lost!")
 #3   
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper, you win!")
        else:
            print("Paper covers rock, You lose!")

   

get_winner(computer_choice, user_choice)

#Task 3 Create a function to simulate the game

def play(get_computer_choice, get_user_choice, get_winner):

    play(get_computer_choice, get_user_choice, get_winner)
