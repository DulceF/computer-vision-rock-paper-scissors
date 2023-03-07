#1 Computer choice

import random
def get_computer_choice():
    
    possible_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(possible_choices)
    return computer_choice

get_computer_choice()

#2 User choice

import cv2
from keras.models import load_model
    
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():  

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
get_prediction()

#3 Countdown

import time
seconds = time.time()
print("You choose {user_choice}", seconds)

 
#4 Figure out who won
#4.1
def get_winner(computer_choice, user_choice):
    while True:  
        if computer_choice == user_choice:
            print("It is a tie!")

        elif computer_choice == "Scissors":
            if user_choice == "Rock":
                print("You won!")
            else:
                print("You lost!")
#4.2        
        elif computer_choice == "Rock":
            if user_choice == "Paper":
                print("You won!")
            else:
                print("You lost!")
 #4.3   
        elif computer_choice == "Paper":
            if user_choice == "Scissors":
                print("You won!")
            else:
                print("You lost!")
   
        get_winner(computer_choice, user_choice)
    

#6. Create a function to simulate the game

def play(get_computer_choice, get_user_choice, get_winner):
    play(get_computer_choice, get_user_choice, get_winner)

computer_wins = "You lost" 
user_wins = "You won"

def rounds_played(computer_wins, user_wins):
    
    if computer_wins == 3:
        print("The game is over, you lost!")
    else:
        user_wins == 3
        print("The game is over, you won")

rounds_played(computer_wins, user_wins)