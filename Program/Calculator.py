import os
whl1=True
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
operations={
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide,
}
while whl1:
    x1=float(input("What is the 1st number?\n"))
    whl=True
    while whl:
          operator=input('''What is the operation you want to perform?
+
-
*
/\n''')
          y1=float(input("What is the next number?\n"))
          answer= operations[operator](x1,y1)
          print(f"{x1} {operator} {y1} = {answer}")
          cont=input("Do you want to continue calculate with the answer or do a new calculation?(Yes/New)\n").lower()
          if cont == "yes":
             whl1=False
          elif cont=="new":
              whl=False
              os.system('cls')
              whl1=True