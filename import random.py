import random

def number_guess_game():
    print("Welcome to Number Guess!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Ask the player to guess the number
            guess = int(input("Your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guess_game()
