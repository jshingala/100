try:
    age = int(input(" What is your age"))
except ValueError:
    print("Write in number form")
    age= int(input("How old are you "))
if age > 18:
    print("You can drive")