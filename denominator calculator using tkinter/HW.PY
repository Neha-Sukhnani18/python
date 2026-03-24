import tkinter as tk
from tkinter import messagebox
import random

# Game rules: rock > scissors, scissors > paper, paper > rock
# The computer's options are mapped to indices 0, 1, 2
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissors"
}

# --- Game Logic Functions ---

def determine_winner(player_choice):
    """Determines the winner of the round."""
    computer_choice_index = str(random.randint(0, 2))
    computer_choice = computer_value[computer_choice_index]

    user_choice_label.config(text=f"Player: {player_choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
    else:
        result = "Computer Wins! 💻"

    result_label.config(text=result)
    disable_buttons()

def disable_buttons():
    """Disables the choice buttons after a match."""
    rock_button["state"] = "disabled"
    paper_button["state"] = "disabled"
    scissors_button["state"] = "disabled"

def reset_game():
    """Resets the game for a new round."""
    rock_button["state"] = "normal"
    paper_button["state"] = "normal"
    scissors_button["state"] = "normal"
    user_choice_label.config(text="Player: Choose an option")
    computer_choice_label.config(text="Computer: Waiting for your move")
    result_label.config(text="Select an option to play a round!")

# --- Tkinter GUI Setup ---

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

# Labels for choices and results
user_choice_label = tk.Label(root, text="Player: Choose an option", font=("Helvetica", 12))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer: Waiting for your move", font=("Helvetica", 12))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Select an option to play a round!", font=("Helvetica", 14, "bold"), fg="blue")
result_label.pack(pady=20)

# Buttons for player choices
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Reset button
reset_button = tk.Button(root, text="Play Again", command=reset_game)
reset_button.pack(pady=10)

# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
