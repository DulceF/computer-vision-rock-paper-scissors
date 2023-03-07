#1 Computer choice

def get_user_choice():
    user_choice = input("What is your choice?: (Rock,Paper or Scissors): ")
    return user_choice
get_user_choice()

import time
seconds = time.time()
print("You choose {user_choice}", seconds)

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

def get_winner(computer_choice, user_choice):
 
#3 Figure out who won
#3.1
    if computer_choice == user_choice:
            print("It is a tie!")

    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You won!")
        else:
            print("You lost!")

#3.2
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
        else:
            print("You lost!")
 #3.3   
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
        else:
            print("You lost!")
   

    get_winner(computer_choice, user_choice)

#4. Create a function to simulate the game

def play(get_computer_choice, get_user_choice, get_winner):

    play(get_computer_choice, get_user_choice, get_winner)
