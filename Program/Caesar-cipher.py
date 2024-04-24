alphabet='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
ans=True
while ans==True:
    direction=input('''Type "Encode" to Encrypt and "Decode" to Decrypt:\n''').lower()
    text=input("Enter your Message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    def cipher(text1,shift1,direction1):
        ca=''
        if direction1=="decode":
                shift1*=-1
        for i in text1:
         if i in alphabet:   
            current_position=alphabet.index(i)
            new_position=current_position+shift1%26
            ca+=alphabet[new_position]
         else:
            ca+=i  
        print(ca)
    cipher(text,shift,direction)
    ques=input("Do you want to continue?(Yes/No)\n").lower()
    if ques=="no":
        ans=False
        print("Goodbye")