 position = alphabets.index(letter)
        new_position = (position + shift) % 26 # this formula word work even it was at the end of the list
        new_letter = alphabets[new_position]
        newLetter += new_letter