import random
import os

def number_game():
    number=random.choice(range(1,101))
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100.")
    difficulty=input("Choose your difficulty:\nType 'easy' or 'hard'.\n").lower()
    if difficulty == "easy":
        attempt=10
    elif difficulty == "hard":
        attempt=5
    print(f"You have {attempt} attempts.")

    guess = int(input("Make a guess: "))

    while attempt>0:
        if guess > number and attempt>0:
            print("Too High.")
            attempt-=1
            print(f"You have {attempt} attempts left.")
        elif guess < number and attempt>0:    
            print("Too Low.")
            attempt-=1
            print(f"You have {attempt} attempts left.")
        elif guess == number:
            print("You win")
            break
        if attempt!=0:
            guess = int(input("Guess again: "))

    if attempt == 0:
        print("You lose.")         

    play_again=input("Do you want to play again.\nType 'Yes' or 'No'.").lower()
    if play_again=="yes":
        os.system('cls')
        number_game()
    elif play_again=="no":
        print("Thank you for playing.")

number_game()
