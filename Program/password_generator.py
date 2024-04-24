X=input("Do you want to generate a password?(Yes/No): ")
if X=="Yes":
    import random
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password=[]
    for n in range(1,nr_letters+1):
     password+=random.choice(letters)
    for n in range(1,nr_numbers+1):
     password+=random.choice(numbers)
    for n in range(1,nr_symbols+1):
     password+=random.choice(symbols)
    random.shuffle(password)
    password=''.join(password)
    print(password)
if X=="No":    
    password=input("Enter your password: ")
    import re

def password_strength_checker(password):
    if len(password) < 8:
        return "Weak: Password is too short, must be at least 8 characters."
    conditions = [
        r'[A-Z]',  # at least one uppercase letter
        r'[a-z]',  # at least one lowercase letter
        r'[0-9]',  # at least one digit
        r'[!@#$%^&*(),.?":{}|<>]'  # at least one special character
    ]
    
    # Initialize the score based on conditions met
    score = 0
    
    # Check each condition and increment the score for each match
    for condition in conditions:
        if re.search(condition, password):
            score += 1
            
    # Determine the strength based on the score
    if score == 4:
        return "Strong: Your password is strong."
    elif score == 3:
        return "Medium: Your password is fairly strong, but could be improved."
    elif score == 2:
        return "Weak: Your password could be much stronger."
    else:
        return "Very Weak: Consider making your password much stronger."
    
# Example usage
password = "ExamplePassword123!"
print(password_strength_checker(password)) 
    