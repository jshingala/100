def bids(bidDict):
    winner= ""
    max = 0
    for i, j in bidDict.items():
        if j > max:
            winner = ix


bidDict = {}
start = True
while start:
    name = input("What is your name?:")
    bid  = int(input(" What is your bid $: "))
    bidDict[name] = bid
    print(bidDict)
    other= input("Are there any other bidders: If y/n").lower()
    if other == 'y':
        start = True
    elif other == 'n':
        start = False
        dict(bidDict)
    else:
        print("Invalid Choice")
    print("\n" * 100 )

