import random
import os
from data_file import data

def cont():
    global A,score
    print("Welcome to Higher or Lower.")
    A=random.choice(data)
    score=0

    def game():
        global A,B,score
        B=random.choice(data)
        while A==B:
            B=data[random.choice(data)]
        print(f'''
Who has got more followers on Instagram?
A:{A['name']} a {A['description']} from {A['country']}.
                        Vs
B:{B['name']} a {B['description']} from {B['country']}.''')
        ans=input("").upper()
        if ans=="A":
            compare(A,B)
        else:
            compare(B,A)

    def compare(a,b):
            global A,B,score
            if a['follower_count']>=b['follower_count']:
                score+=1
                os.system('cls')
                print(f"You are right. Your current score is: {score}")
                A=B
                game()
            else:
                os.system('cls')
                print(f"You are wrong. Your final score is: {score}")
            
    game()

    play=input("Do you want to play again?(Yes/No)").lower()
    if play=="yes":
         os.system('cls')
         cont()
    else:
         print("Thank you for playing.")

cont()