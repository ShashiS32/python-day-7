import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

letter_guess = input("Guess a letter: ").lower()

for letter in chosen_word:
  if letter == letter_guess:
    print("Right")