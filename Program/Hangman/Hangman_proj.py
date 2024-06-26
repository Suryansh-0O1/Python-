import os
import random
import hangman_words
import hangman_art
chosen_word = random.choice(hangman_words.wordlist)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []
print(hangman_art.logo)
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    if guess in display:
      print("You have already guessed this letter.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f'''You lose.
The word was: {chosen_word}''')
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])