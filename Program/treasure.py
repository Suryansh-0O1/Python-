print("""

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_|.-'
""")      
print("Welcome to Treasure Island")
print("Your task is to find the The Treasure.")
X=input("Where do you want to go?(Left or Right).\n")
X=X.lower()
if X=="left":
 Y=input("There's an ocean in front of you.\nWhat do you want to wait or do you want to swim?\n")
 Y=Y.lower()
 if Y=="wait":
   Z=input("A boat appeared you took the boat and dropped you on a Island.\nThere's a room infront of you.\nYou enter the room.\nThere are three doors in front of you(Red,Yellow,Blue).\nChoose a room.\n")
   Z=Z.lower()
   if Z=="Red":
     print("You were caught in a fire.\nYou died.\nGame Over.")
   elif Z=="blue":
     print("You drowned in the lake inside.\nGame Over.")
   elif Z=="yellow":
     print("You found the treasure chest.\nYou open it and found gold.\nYou Won.")
 else:
   print("A shark attacked you.\nYou died.\nGame Over.")  
else:
 print("You fell into a ditch.\nGame Over.")

 