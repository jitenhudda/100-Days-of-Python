# Guessing Game

#random.randint(a,b)  
#(a: int, b: int) -> int
#Return random integer in range [a, b], including both end points

#print(random.randint(1,400))  # - check number is random given or not b/w 1 to 400 this range is anything given


import random
jackpot = random.randint(1,100)

guess = int(input("number guess krr"))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")
    
    guess = int(input("fir se guess krr"))
    counter+=1

print("shi guess kiya")
print("you took",counter, "attempts")