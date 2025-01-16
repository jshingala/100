


def add(n1, n2):
    return n1, n2
def divide(n1, n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
def subtract(n1, n2):
    return n1-n2

n1= float(input("Enter the first number"))
print("+\n-\n*\n/\n")
operation = (input("Pick an operation"))

n2= float(input("Enter the secound number"))
def result():
    if operation == "+":
        result= add(n1,n2)
    elif operation == "-":
        result= subtract(n1,n2)
    elif operation == '*':
        result= multiply(n1, n2)
    elif operation == "/":
        result= divide(n1, n2)
    else:
        result= "Invalid choice"

    print(f"The result is {result}")

result()
