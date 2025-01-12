print("Welcome to the bill checker")

amount = float(input("Enter the bill amount"))

if amount >=20:
    print("It is overbudget")
else:
    print("Go for it")


print("Odd and even Checker")
number = int(input("Enter the integer number"))

if number%2 == 0:
    print("It is Even")

else:
    print("It is Odd")
bill =0
age = 65

if age< 12:
    bill = 5
    print("$ please")

elif age <=18:
    bill = 8
    print("8$ please")

elif age>=45 and age<=67:
    print("Enjot the ride is on us ")

else:
    bill = 9
    print("9$please")

photo= input("Do you want the picture(y/n)")
if photo=='y':
    bill+= 3
    print(bill)