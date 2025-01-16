def name(fname, lname):
    fName= fname.title()
    lName = lname.title()
    return f"{fName} {lName}"



print(name("jenil", "shingala"))

def gas(mileage, gas_available):
    return mileage * gas_available

mileage = float(input("What is your mileage (miles per gallon)? "))
gas_available = float(input("How much gas is available (gallons)? "))

max_distance = gas(mileage, gas_available)
print(f"The maximum distance you can travel is {max_distance:.2f} miles.")