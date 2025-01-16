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
    else:
        while True:
            check = input(f"The total is {total}. Do you want to hit ('h') or stand ('s')? ").lower()
            if check == 's':
                print(f"You chose to stand. Final cards: {randomChoice}, total: {total}")
                break
            elif check == 'h':
                randomChoice2 = random.choice(cards)
                randomChoice.append(randomChoice2)
                total = sum(randomChoice)
                print(f"You drew {randomChoice2}. Your cards are now {randomChoice}, total: {total}")

                if total == 21:
                    print("BlackJack!")
                    break
                elif total > 21:
                    print("Bust! You went over 21.")
                    break
            else:
                print("Invalid input. Please type 'h' to hit or 's' to stand.")


gameOver()