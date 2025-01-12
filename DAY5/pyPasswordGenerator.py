import random
letters = ['a','b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x', 'y', 'z']
numbers = ['0','1','2','3','4','5', '6', '7', '8','9']
symbols =  ['!','#','$','%','&','(',')', '*', ']', '[']

encLetters= int(input("Enter how many letters you need in the password "))
encNumbers= int(input("Enter how many numbers you need in your paswword "))
encSymbols= int(input("Enter how many special character you need in your password "))

# Easy mode(sequentional) and also hard method is done 
password = ""

for i in range(encLetters):
    password += random.choice(letters)

for i in range(encNumbers):
    password +=  random.choice(numbers)

for i in range(encSymbols):
    password += random.choice(symbols)

passer = ''.join(random.sample(password, len(password)))

print(f"Your strong password is {passer}")
