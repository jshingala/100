def find_winner(bidDict):
    """
    Function to find the winner with the highest bid.
    Args:
    - bidDict (dict): A dictionary containing names as keys and bids as values.
    """
    winner = ""
    max_bid = 0
    for name, bid in bidDict.items():
        if bid > max_bid:
            max_bid = bid
            winner = name
    print("\n"*100)
    print(f"The winner is {winner} with a bid of ${max_bid}.")

# Initialize an empty dictionary to store bids
bidDict = {}
start = True

# Start the bidding process
while start:
    name = input("What is your name?: ")
    bid = int(input("What is your bid $: "))
    bidDict[name] = bid  # Add the name and bid to the dictionary
    # Display the current bids
    
    # Check if there are other bidders
    other = input("Are there any other bidders? (y/n): ").lower()
    if other == 'y':
        start = True  # Continue the loop
        print("\n" * 100)
    elif other == 'n':
        start = False  # End the loop
        find_winner(bidDict)
        # Call the function to find the winner
    else:
        print("Invalid choice.")
    
    # Clear the console (simulated with newlines)
    
