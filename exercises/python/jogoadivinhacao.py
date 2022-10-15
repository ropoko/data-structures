import random

number = random.randint(1,10)
user = 0
count = 0

while user != number and user != "exit":
    user = int(input("What's your guess? "))
    
    if user == "exit":
        break
    
    count += 1
    
    if user < number:
        print("Too low!")
    elif user > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")