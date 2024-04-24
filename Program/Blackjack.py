import random
import os
my_cards=[]
dealer=[]
card_list=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
whl1=True
def dealing_cards(my_cards1,dealer1):
    """Dealing cards"""
    my_cards1 = my_cards.extend(random.sample(card_list,2))
    dealer1 = dealer.extend(random.sample(card_list,2))
    return (my_cards1,dealer1)
def add(my_list):
    """Card Sum"""
    my_cards_sum1 =sum(my_list)
    if my_cards_sum1 > 21 and 11 in my_list:
        my_list.remove(11)
        my_list.append(1)
        my_cards_sum1 = sum(my_list)
    return (my_cards_sum1)
def clr():
    os.system('cls')
    print(f"Dealer cards are:\n{dealer}")
    print(f"Your cards are:\n{my_cards}")
def calc():
    """Dealing dealer cards when dealer<my_cards"""
    whl2=True
    while whl2:
        dealer.append(random.choice(card_list))
        my_cards_sum,dealer_sum=add(my_cards),add(dealer)
        clr()
        if dealer_sum<21 and dealer_sum<my_cards_sum:
            whl2=True
        elif dealer_sum>21:
            clr()
            print("You win")
            whl2=False
        elif dealer_sum == 21:
            clr()
            print("You lose")
            whl2=False    
        elif dealer_sum>my_cards_sum:
            clr()
            print("You lose")
            whl2=False 
def blackjack():
    """Basic function of comparing"""
    my_cards_sum,dealer_sum=add(my_cards),add(dealer)
    if dealer_sum>my_cards_sum:
        clr()
        print("You lose")
    elif dealer_sum==my_cards_sum:
        clr()
        print("You lose")
    elif dealer_sum < my_cards_sum:
        calc()        
#Starring definattion
my_cards_sum = 0
dealer_sum = 0
dealing_cards(my_cards,dealer)
first_dealer_card=dealer[1]
print(f"Dealer cards are:\n[X,{first_dealer_card}]")
print(f"Your cards are:\n{my_cards}")
my_cards_sum,dealer_sum=add(my_cards),add(dealer)
if my_cards_sum==21 and 11 in my_cards and 10 in my_cards:
    blackjack()
    whl1=False

#Main game
while whl1:
    more_cards=input("Do you want to Hit or Stand?").lower()
    if more_cards == "hit":
        my_cards.append(random.choice(card_list))
        os.system('cls')
        print(f"Dealer cards are:\n[X,{first_dealer_card}]")
        print(f"Your cards are:\n{my_cards}")
        my_cards_sum,dealer_sum=add(my_cards),add(dealer)
        if my_cards_sum < 21:
            whl1=True
        elif my_cards_sum==21:
            blackjack()
            whl1=False
        elif my_cards_sum > 21:
            print("It's a bust")
            whl1=False
    elif more_cards == "stand":
        blackjack()
        whl1=False