import tkinter as tk
from tkinter import messagebox
import random

# This is a method to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to handle user choice
def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    # Update the display
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

    # Update scores and display result
    if result == "tie":
        result_label.config(text="It's a tie!")
    elif result == "user":
        result_label.config(text="You win!")
        global user_score
        user_score += 1
    else:
        result_label.config(text="You lose!")
        global computer_score
        computer_score += 1

    # Update score labels
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer's score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="Result: ")
    user_score_label.config(text="Your score: 0")
    computer_score_label.config(text="Computer's score: 0")
# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
# Create a global variable to keep track of the scores
# Initialize scores
user_score = 0
computer_score = 0
# Create the widgets
title_label = tk.Label(root, text="Let's Play Rock-Paper-Scissors", font=("Arial", 16))
title_label.pack(pady=10)
# Create a label to display the user's choice
user_choice_label = tk.Label(root, text="Your choice: ", font=("Arial", 12))
user_choice_label.pack()
# Create a label to display the computer's choice
computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Arial", 12))
computer_choice_label.pack()
# Create a label to display the result of the game
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)
# Create a label to display the user's score
user_score_label = tk.Label(root, text="Your score: 0", font=("Arial", 12))
user_score_label.pack()
# Create a label to display the computer's score
computer_score_label = tk.Label(root, text="Computer's score: 0", font=("Arial", 12))
computer_score_label.pack()
# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
# Rock button
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)
# Paper button
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)
# Scissors button
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)
# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)
# Run the main loop
root.mainloop()