def myFunction():
    print("Welcome to day 6")
    numChar = (len("Hello"))

myFunction()

# Done rest of the code in the
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hoop():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def total():
    if wall_in_front() == True:
            hoop()
    elif front_is_clear() == True:
        move()
while at_goal() != True:
    total()
'''

#Hurdle 4
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def round_corner():
    turn_right()
    move()
    turn_right()

def jump():
    turn_left()
    while wall_on_right():
        move()
    round_corner()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''