#sorteando numeros
import random

user = input('Number: ')
x = random.randrange(0, 1000)
y = str(x)

print('You: ' + user)
print('Machine: ' + y)

if x > int(user):
    print('machine wins! :D')
else:
    print('You wins! :D')
