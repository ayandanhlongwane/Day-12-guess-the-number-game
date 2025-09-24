python
import random

number_to_guess = random.randint(1, 50)
guess = None
attempts = 0

print("🎯 Guess the number (between 1 and 50)")

while guess != number_to_guess:
    try:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")
