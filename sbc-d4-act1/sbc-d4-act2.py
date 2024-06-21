# Importing Randint to Random to generate random numbers
from random import randint

# Getting User Input like 0 hayang 1 kulob
ako = int(input("enter 0 hayang to  1 kulob: "))

#randomly Generate Number for c2 and c3
c2 = randint(0,1); c3 = randint(0,1)

# To identify that 0 is kulob and 1 is hayang 
choices = {0: "kulob", 1: "hayang"}

# Print the choices for user 'ako' 'c2' and 'c3'
print (f"ako: {choices [ako]}")
print (f"c2: {choices [c2]}")
print (f"c3: {choices [c3]}")

# Determine the winner based on the combination of the choices 
outcome = {
    (0, 1, 1): "You Win", (1, 0, 0,): "You Win",
    (1, 0, 1): "C2 Wins", (0, 1, 1,): "C2 Win",
    (1, 1, 0): "C3 Wins", (0, 0 , 1): "C3 Win"
    }

# If the key (ako, c2, c3) does not exist in the outcomes dictionary, it returns value "Draw".
print(outcome.get((ako,c2,c3), "Draw"))