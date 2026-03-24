import random

def play_game():
    """
    This function contains the main game logic for Rock, Paper, Scissors.
    It uses a while loop to allow for continuous play until the user decides to stop.
    """
    player_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors! Rock beats scissors, scissors beat paper, and paper beats rock.\n")

    # Main game loop
    while True:
        # Get player input and validate it
        player_choice = None
        while player_choice not in options:
            player_choice = input("Enter a choice (rock, paper, scissors) or 'q' to quit: ").lower()
            if player_choice == 'q':
                break
            if player_choice not in options:
                print("Invalid choice. Please try again.")
        
        if player_choice == 'q':
            break

        # Get computer's random choice
        computer_choice = random.choice(options)
        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print(f"You win! {player_choice.capitalize()} beats {computer_choice}.")
            player_wins += 1
        else:
            print(f"You lose. {computer_choice.capitalize()} beats {player_choice}.")
            computer_wins += 1

        # Display current scores
        print(f"\nYour wins: {player_wins}, Computer wins: {computer_wins}")

        # Ask to play again
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes" and play_again != "y":
            print("Thanks for playing!")
            break

    print("\nFinal Score:")
    print(f"You: {player_wins} | Computer: {computer_wins}")

if __name__ == "__main__":
    play_game()
