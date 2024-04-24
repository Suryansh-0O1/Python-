rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
X=int(input("Choose 0 for rock, 1 for paper and 2 for scissors: "))
import random
Y=random.randint(0,2)
P=[rock, paper, scissors]
if X>=0 and X<=2 and Y>=0 and Y<=2: 
 print(f"The user choose {P[X]}")
 print(f"The Computer choose {P[Y]}")
 if X==0 and Y==2:
     print("You Win.")
 elif Y==0 and X==2:
     print("You lose.")
 elif Y>X:
     print("You lose")
 elif X>Y:
     print("You win.")
 elif X==Y:
     print("You drew.")
else:
 print("You chose a wrong number")



