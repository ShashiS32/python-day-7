import random

word_list = ['aarvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

wordlength = len(chosen_word)

lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


display = []

for i in range (wordlength):
  display += "_"

endofgame = False

while not endofgame:
  guess = input("Guess a letter in the word: ").lower()



  for position in range(wordlength):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    print(stages[lives])
    if lives == 0:
      endofgame = True
      print("You lost")

  print(display)


  
  if "_" not in display:
    endofgame = True
    print("You win")