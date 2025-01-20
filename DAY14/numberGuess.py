import random
from higher_lower_game import data
from art import logo, vs

def randomAccount():
    return random.choice(data)
def printData(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"
def check(guess, accountA, accountB):
    return (accountA > accountB and guess == "a") or (accountB > accountA and guess == "b")

def game():
    accountB= randomAccount()
    game_continue = True
    points= 0

    while game_continue:
        accountA = accountB
        accountB = randomAccount()

        print(f"Compare A:{printData(accountA)} ")
        print(vs)
        print(f"Against B: {printData(accountB)}")

        guess = input("Who has more folowers? A or B").lower()
        correct = check(guess, accountA, accountB)
        print(logo)
        if correct:
            points += 1
            print(f"You are right{points}")
        else:
            game_continue = False
            print(f"Wrong your score come out to be {points}")
game()