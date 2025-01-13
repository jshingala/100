alphabets = ['a','b','c','d','e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type decode to 'decrypt':\n")
text = input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))


def encrypt():
    for letter in text:
        position = alphabets.index(letter)
        new_position = (position + shift) % 26
        new_letter = alphabets[new_position]
        print(new_letter)

if direction == "encode":
    encrypt()