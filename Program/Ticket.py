height=int(input("What is your height in cm? "))
bill=0
if height>=120:
    age=int(input("What is your age? "))
    if age<12:
        bill=50
        print("Your ticket is the kid's ticket")
    elif age>12 and age<18:
        bill=100
        print("Your ticket is the teen's ticket")
    else:
        bill=150
        print("Your ticket is the adult's ticket")
    photo=input("Do you want a photo? (Yes/No) ")
    if photo=="Yes":
        bill+=3
        print(f"Your bill is Rs{bill}")
    else:
        print(f"Your bill is Rs{bill}")
else:
    print("Not sufficient height")        
