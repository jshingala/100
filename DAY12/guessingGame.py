import random

print("Welcome to the guessing game! Guess a number between 1 and 100")
level = input("Enter the mode: 'e' for easy, 'm' for medium, 'h' for hard: ").lower()
randomNumber = random.randint(1, 100)  # Generate a random number

if level == 'e':
    tries = 5
elif level == 'm':
    tries = 3
elif level == 'h':
    tries = 1
else:
    print("Invalid level choice. Defaulting to easy mode.")
    tries = 5


while tries > 0:
    print(f"You have {tries} guesses left.")
    guess = int(input("Guess the number: "))
    if guess == randomNumber:
        print("Congratulations! You guessed the correct number!")
        break  
    elif guess > randomNumber:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    tries -= 1  


if tries == 0:
    print(f"You lost. You are out of tries. The correct number was {randomNumber}.")

