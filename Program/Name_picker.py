names_string=input("Enter names seperated by ',' and a space: ")
names = names_string.split(", ")
import random
X=len(names)-1
Y=random.randint(0,X)
Z=names[Y]
print(f"{Z} is going to buy the meal today!") 