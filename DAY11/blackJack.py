import random

def gameOver():
    game= (input("Do you wanna play the game 'y' or 'n'"))
    if game == 'y':
        print("You are in ")
        gamePart1()
    elif game == 'n':
        print("Bye")
    else:
        print("Invalid Choice")

def gamePart1():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    randomChoice= random.choices(cards, k =2)
    print(randomChoice)
    total = sum(randomChoice)
    if total == 21:
        print("BlackJack")


gameOver()