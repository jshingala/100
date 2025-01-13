import art as art 
print(art.logo)



def encrypt(originalText, shiftAmount):
    newLetter = ""
    for letter in originalText:
        if letter == " ":
            newLetter += letter
        else:
            position = alphabets.index(letter)
            new_position = (position + shiftAmount) % 26
            newLetter+= alphabets[new_position]
            
    print(f"The encoded code is {''.join(newLetter)}")
def decrypt(originalText, shiftAmount):
    newLetter = ""
    for letter in originalText:
        if letter == " ":
            newLetter += letter
        else:
            position = alphabets.index(letter)
            new_position = (position - shiftAmount) % 26
            newLetter+= alphabets[new_position]
    print(f"The decoded message is { ''.join(newLetter)}")

def caeser(originalText, shiftAmount, encodeOrDecode):
    newLetter = ""
    for letter in originalText:
        if letter not in alphabets:
            newLetter += letter
        else:
            position = alphabets.index(letter)
            if encodeOrDecode == 'decode':
                new_position = (position - shiftAmount) % 26
            elif encodeOrDecode == 'encode':
                new_position = (position + shiftAmount) % 26
            newLetter+= alphabets[new_position]
    print(f"The {encodeOrDecode}d message is { ''.join(newLetter)}")

shouldConinue= True
while shouldConinue:
    alphabets = ['a','b','c','d','e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    direction = input("Type 'encode' to encrypt, type decode to 'decrypt':\n")
    text = input("Type your message:\n").lower()
    shift= int(input("Type the shift number:\n"))

    caeser(originalText= text, shiftAmount= shift, encodeOrDecode= direction )
    restart = input("Do you wanna go again if (Y or N):\n").lower()
    if restart == 'y':
        shouldConinue =True
    elif restart == 'n':
        shouldConinue = False
    else:
        print("Invalid Choice")