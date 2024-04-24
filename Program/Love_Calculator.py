print("The Love Calculator is calculating your score...")
name1 = input("What's the first person's name? ")
name2 = input("What's the second person's name? ")
name=name1+name2
x=name.lower()
t=x.count("t")
r=x.count("r")
u=x.count("u")
e=x.count("e")
a=t+r+u+e
l=x.count("l")
o=x.count("o")
v=x.count("v")
b=l+o+v+e
c=str(a)+str(b)
c=int(c)
if c<10 or c>90:
  print(f"Your score is {c}, you go together like coke and mentos.")
elif c>40 and c<50:
  print(f"Your score is {c}, you are alright together.")
else:
  print(f"Your score is {c}.")