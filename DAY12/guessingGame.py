import random 

    




print("Welcome to guessing game Guess a number between 1 and 100")
level= input("Enter the mode 'e' for easy , 'm' for medium, 'h' for hard").lower()
randomNumber = random.randint(1,100)


if level == 'e':
    guess =  int(input("Guess the number "))
    if guess == randomNumber:
        print("You won the game ")
    elif guess > randomNumber:
        print("The number is too high")
    elif guess < randomNumber:
        print("The guess is too low ")