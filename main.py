#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


lives = 5

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print (f"{' '.join(display)} \n")

end_of_game = False

wrong_guess = []

while not end_of_game:    
    guess = input("Guess a letter: ").lower()
    
    
    

    if guess not in chosen_word:
        lives = lives - 1
        wrong_guess.append(guess)
        print(f"You have {lives} lives left \n")
        print (f"{' , '.join(wrong_guess)} are your wrong guesses \n")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print (f"{' '.join(display)} \n")
    print(f"You have {lives} lives left \n")
    if len(wrong_guess) == 0:
        print ("You have no wrong guesses \n")

        
    if lives == 0:
        print("You Lose")
        exit()
    if "_" not in display:
        print("You win!")
        exit()




