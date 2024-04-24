print("Thank you for choosing Python Pizza Deliveries!")
size = input("What's the size of pizza you want?(Small/Medium/Large) ") 
add_pepperoni = input("Do you want to add pepperoni?(Yes/No) ")
extra_cheese = input("Do you want to add cheeze?(Yes/No) ") 
bill=0
if size=="Small":
 bill=15
 if add_pepperoni=="Yes":
  bill+=2
elif size=="Medium":
 bill=20
 if add_pepperoni=="Yes":
  bill+=3
else:
 bill=25
 if add_pepperoni=="Yes":
  bill+=3
if extra_cheese=="Yes":
 bill+=1
print(f"Your final bill is: ${bill}.")