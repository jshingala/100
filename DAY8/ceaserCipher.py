alphabets = ['a','b','c','d','e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type decode to 'decrypt':\n")
text = input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))

def encrypt():
    newLetter = []
    for letter in text:
        if letter == " ":
            newLetter.append(letter)
        else:
            position = alphabets.index(letter)
            new_position = (position + shift) % 26
            new_letter = alphabets[new_position]
            newLetter.append(new_letter)
    print(''.join(newLetter))

if direction == "encode":
    encrypt()