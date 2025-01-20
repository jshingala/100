def fun():
    for i in range(1,21):
        if i == 20:
            print("You got it")
def checker():
    year = int(input("What is the year"))
    if year> 1980 and year <= 2000:
        print("You are old")
    elif year > 2000:
        print("You are gen Z")

checker()