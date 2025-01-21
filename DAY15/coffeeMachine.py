MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


while True:
    try:
        userInput = input("Enter your choice ('e' for Espresso, 'l' for Latte, 'c' for Cappuccino and q to quit): ").strip().lower()

        if userInput == 'e':
            print("Indeed you are getting the espresso shots")
            break
        elif userInput == 'l':
            print("You are getting your Latte")
            break
        elif userInput == 'c':
            print("Indeed you are getting your Cappuccino")
            break
        elif userInput == 'q':
            print("Thank you so much I hope you have a great day ahead")
            break
        else:
            raise ValueError("Invalid input. Please enter 'e', 'l', or 'c'.")
    except ValueError as e:
        print(f"Error: {e}")
