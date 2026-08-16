# Guess-the-number

A simple command-line game written in Python. The computer chooses a random number from 1 to 100, and the player keeps guessing until they find it.

How the game works

Enter a number between 1 and 100.

If the guess is too high, the game asks for a lower number.

If the guess is too low, the game asks for a higher number.

When the number is correct, the game displays the total number of attempts.

Requirements

Python 3

No external packages are required.

Run the game

Save the Python code as guess_the_number.py.

Open a terminal in the same folder.

Run:

python guess_the_number.py

On some systems, use python3 instead:

python3 guess_the_number.py

Python code

import random

number = random.randint(1, 100)
guesses = 0
guess = None

while guess != number:
    guess = int(input("Guess the number: "))
    guesses += 1

    if guess > number:
        print("Lower number, please.")
    elif guess < number:
        print("Higher number, please.")

print(f"You guessed the number {number} correctly in {guesses} attempts!")

Example

Guess the number: 70
Lower number, please.
Guess the number: 40
Higher number, please.
Guess the number: 55
You guessed the number 55 correctly in 3 attempts!

Possible improvements

Reject input outside the 1–100 range.

Handle non-numeric input without crashing.

Add difficulty levels or a maximum number of attempts.

Let the player start another round.

License

This project is free to use for learning and practice.
