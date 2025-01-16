def cal():
    def add(n1, n2):
        return n1 + n2
    def mul(n1, n2):
        return n1 * n2
    def div(n1,n2):
        return n1/n2
    def sub(n1, n2):
        return n1-n2
    

    def cal2(n1):

        print("+\n-\n*\n/\n")
        operation= input(("What operation you wanna do "))
        n2 = int(input("Enter the number2"))

        if operation == "+":
            result = add(n1,n2)
        elif operation == "-":
            result = sub(n1, n2)
        elif operation == "*":
            result = mul(n1,n2)
        elif operation == "/":
            result = div(n1,n2)
        else:
            print("Invalid choice choose another option ")
        j=input(f"The result is the {result} . Do you wanna continue y or n")
        print(j)
        if j == "y":
            cal2(result)
        if j == "n":
            cal()
            
    n1= int(input("Enter the number"))
    cal2(n1)


cal()