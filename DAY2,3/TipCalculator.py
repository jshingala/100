import random

print("Calculator for Tip")
bill = random.randint(20, 200)  # Random bill amount between $20 and $200
print(f"The total bill is: ${bill}")

# Ask the user for the tip percentage
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

# Calculate the tip and total amount
tip = bill / 100 * tip_percentage
total_amount = bill + tip

print("Do you wanna split the bill? (Y/N)")
split_bill = input().strip().lower() == "y"

if split_bill:
    # Ask how many people to split the bill
    num_people = int(input("How many people to split the bill? "))
    if num_people > 0:
        amount_per_person = total_amount / num_people
        print(f"The total bill including tip is: ${total_amount:.2f}")
        print(f"Each person needs to pay: ${amount_per_person:.2f}")
    else:
        print("Invalid number of people.")
else:
    print(f"The tip amount is: ${tip:.2f}")
    print(f"The total bill including tip is: ${total_amount:.2f}")
