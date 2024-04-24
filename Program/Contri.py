money=float(input("Enter your bill amount: "))
tip=float(input("Enter the tip percentage (10/12/15): "))
people=float(input("Enter the number of people: "))
contri=round(money*(tip/100+1)/people,2)
contri="{:.2f}".format(contri)
print(f"Each person contribution is {contri}")
  