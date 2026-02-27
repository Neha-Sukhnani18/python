import random
def guess_the_number():
    """A simple number guessing game in Python."""
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    guess = None
    print(f"Welcome to the Number Guessing Game!")
    print(f"I am thinking of a number between {lower_bound} and {upper_bound}.")
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")
            continue 
    print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
if __name__ == "__main__":
    guess_the_number()