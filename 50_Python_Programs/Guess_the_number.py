import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Allow the player to make up to 3 guesses
for attempt in range(3):
    # Get the player's guess
    guess = int(input("Guess the number (between 1 and 10): "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")

# Display the correct number if the player couldn't guess it
else:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
