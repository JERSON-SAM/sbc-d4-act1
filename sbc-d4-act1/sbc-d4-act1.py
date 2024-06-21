#Import Randint to random to generate random numbers
from random import randint

# Print the Value then Enter Number 
print ("E Enter Ang Una na Number:"); una = int(input())
print ("E Enter Ang Ikaduha na Number:"); duha = int(input())
print ("E Enter Ang Ikatulo na Number:"); tulo = int(input())

# User need to enter their lucky Number
bet = [una,duha,tulo]
print ("Your Bet: ", una, duha, tulo)

#Generate Random Result in Range of 3
result = [randint(1,3) for _ in range(3)]

# If your Lucky Number is targeted the result you win 
if bet == result:
    game_result = ("Daug Ka!")

#If your Lucky number is not targeted the result but its rumble you partially win
elif set(bet) == set(result):
    game_result = ("Daug Ka Rumble")

#If your lucky number is not targeted you lost.
else:
    game_result = ("pilde ka! haha")

# Print the result and the game_result
    print(f"result: {result}")
    print(game_result)

