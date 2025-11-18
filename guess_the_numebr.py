import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")
    attempts += 1
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {number}. You guessed it in {attempts} tries.")
        break
