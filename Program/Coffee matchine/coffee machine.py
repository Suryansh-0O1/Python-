from menu import MENU,resources
import os


quarters = 0.25 
dimes = 0.10 
nickles = 0.05 
pennies = 0.01
c=False

def get_order():
    global choise


    def check_resources():
        global choise,c
        for i in MENU[choise]['ingredients']:
            if MENU[choise]['ingredients'][i] > resources[i]:
                print(f"Sorry not enough {i} available.\nAsk for a refill.")
                c = False
                break
            elif MENU[choise]['ingredients'][i] < resources[i]:
                c=True
            
        if c:
             ask_of_money() 


    def ask_of_money():
        global quarters,dimes,nickles,pennies,choise
        print(f"Your bill is: ${MENU[choise]['cost']}")
        quarter=int(input("Enter Quarters: "))
        dime=int(input("Enter Dimes: "))
        nickel=int(input("Enter Nickles: "))
        pennie=int(input("Enter Pennies: "))

        money= (quarter*quarters + dime*dimes + nickel*nickles + pennie*pennies)

        if money>=MENU[choise]['cost']:
            change= round((money- MENU[choise]['cost']),2)
            new_resources()
            print(f"Here's your change: ${change}\nEnjoy your {choise}.")
        else:
            print("Sorry not enough money, heres's your refund.")


    def new_resources():
        global choise
        for i in MENU[choise]['ingredients']:
            resources[i] = resources[i]-MENU[choise]['ingredients'][i]
    
    
    choise=input("What would you like to drink? (Espresso/Latte/Cappuccino) \n").lower()
    
    orders=["espresso","latte","cappuccino"]

    functions=["refill","resource","off"]

    if choise in orders:
        check_resources()
    
    elif choise in functions:
        if choise == "resource":
            print(resources)
            get_order()
        elif choise == "refill":
            resources['water']=300
            resources['milk']=200
            resources['coffee']=100
            os.system('cls')
            get_order()
        elif choise == "off":
            os.system('cls')
            exit()   
    else:
        os.system('cls')
        print("Sorry I didn't recognised that.")
        get_order()
    
    new_order = input("Do you want to order again? (Yes/No)\n").lower()
    if new_order=="yes":
        get_order()
    elif new_order=="no":
        os.system('cls')
        get_order()
    else:
        os.system('cls')
        print("Sorry I didn't recognised that.")
        get_order()


get_order()



