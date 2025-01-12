# Day 4 Project 

print('''Addams Family Mansion      _____
                                    )   (
                                    / oOo \
                                    /_______\
                                    L       A
                                    E  .-.  M
                                    S  |~|  C
            I-I-I-I-I-I-I-I-I-I-I-I-T  |_|  |I-I-I-I-I-I-I-I-I-I-I-I-I
            ).**.(~~~~~~~~~~~~~~~~~~E       |~~~~~~~~~~~~~~~~~~~).**.(
            / |  | \                 R       |                  / |  | \
            ) |__| (                _|_.---._|_                 ) |__| (
            |______|_________________|' .-. '|__________________|______|
            |      |  .-.  .-.       |,-|~|-,|        .-.  .-.  |      |
            \ .    /  |~|  |~|       || | | ||        |~|  |~|  \    . /
            )H   (   |_|  |_|       ||_|_|_||        |_|  |_|   )   H(
            |    |                  |       |                   |    |
            |    |                  |       |                   |    |
            \    /   ...  ...       |_.=~=._|        ...  ...   \    /
            ). (    |~|  |~|       |I|   |I|        |~|  |~|    ) .(
            |H |    |_|  |_|       |I|  .|I|        |_|  |_|    | H|
            |  |                   |I|___|I|                    |  |
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
''')




print("Welcome to the game")
print("Your mission is to find the treasure ")
choice1= input('You are at a crossward, where do you want to go (left or right)').lower()
if choice1 == 'left':
    choice2= input('You see a big lake and nothing you can see in the nearby site choose "wait" or "swim"').lower()
    if choice2 == 'wait':
        choice3 =print('Now you see that somebody helped you to reach the castle now you see three doors "red" "blue" "green"')
        if choice3 == 'green':
            print("You found the treasure ")
        else:
            print("You found a dragon")
    else:
        print("You drowned you lost sorry about that ")
else:
    print("You have fell into the hole. Game Over")