line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")   
W=position[0].lower()
abc=["a","b","c"]
Y=abc.index(W)
Z=int(position[1])-1
map[Z][Y]="X"
print(f"{line1}\n{line2}\n{line3}")