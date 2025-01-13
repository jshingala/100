import random


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

for i in HANGMANPICS:
    print(i)

wordsList = ['Hangman', 'Shinchan', 'Fruits' , 'Burrito', 'Doggy', 'Harry', 'Berries']

randomWord = random.choice(wordsList)

gameChar = []

for i in randomWord:
    print(i)
    gameChar += '-'

print(gameChar)

count = 0
gameOver = True
while gameOver:
   print(' '.join(gameChar))
   userGuess = input("Enter a single letter: ").strip()[0]

   letter_found = False
   for i in range(len(randomWord)):
       if randomWord[i] == userGuess:
           gameChar[i] = userGuess
           letter_found = True
           print(HANGMANPICS[count])

   if not letter_found:
       count += 1
       print("You lost a life")
       if count < len(HANGMANPICS):
           print(HANGMANPICS[count])
       else:
           print("Game Over!")
           gameOver = False

   if '-' not in gameChar:
       print("Congratulations! You won!")
       print("The word was:", randomWord)
       gameOver = False