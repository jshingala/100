import random
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, Scissor]
user = int(input("Enter your choice rock, paper or scissor by the order of (1,2,3) "))
if 1<= user <=3:
    print(" You choose")
    print(game[user -1])
else:
    print("Invalid choice")
    exit("Try again")


random= random.choice(range(0,2))
print(f"computer choose {game[random]}")

if user -1 == random:
    print("It is a Tie")
elif (random== 0 and user == 3) and (random == 1 and user == 1) and (random ==2 and user ==2):
    print("Computer wins")
else:
    print("You win")