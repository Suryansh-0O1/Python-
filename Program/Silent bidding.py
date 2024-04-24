import os
ans=True
blist={}
def participant(name1,price1):
        blist[name1] = price1
while ans:
    name=input("What is your name?:\n")
    price=int(input("What's your highest bid?:\n$"))
    participant(name,price)
    ques=input("Are there more people?(Yes/No):\n").lower()
    if ques=="no":
        os.system('cls')
        ans=False
    elif ques=="yes":
         ans=True
         os.system('cls')   
i=0
nam=''
for key in blist:
     if blist[key]>i:
          i = blist[key]
          nam=key
print(f"The Winner is {nam} with a bid of ${i}")          