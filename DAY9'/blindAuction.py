


start = True
while start:
    name = input("What is your name?:")
    bid  = int(input(" What is your bid $: "))
    other= input("Are there any other bidders: If y/n").lower()
    if other == 'y':
        start = True
    elif other == 'n':
        start = False
    else:
        print("Invalid Choice")
    print("\n" * 100 )

