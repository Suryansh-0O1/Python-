from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

menu=Menu()
coffeemaker=CoffeeMaker()
moneymachine=MoneyMachine()
list=["off","profit","resource"]
whl=True
while whl:
    choise = input(f"Please enter your order:\n({menu.get_items()})\n").lower()
    if choise in list:
        if choise=="off":
            os.system('cls')
            exit()
        elif choise == "profit":
            moneymachine.report()
        elif choise == "resource":
            coffeemaker.report()
    else:
        drink = menu.find_drink(choise)
        check=coffeemaker.is_resource_sufficient(drink)
        if check:
            print(f"Your coffee cost is: {drink.cost}")
            enter_money = moneymachine.make_payment(drink.cost)
            if enter_money:
                coffeemaker.make_coffee(drink)
            else:
                whl=False
                exit()
        else:
            whl=False
            exit()
    ask=input("Do you want to order again? (Yes/No)").lower()
    if ask == "yes":
        whl=True
    else:
        os.system('cls')
        whl=True

