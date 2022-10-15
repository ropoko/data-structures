a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

newlist = []

for x in a:
    if x < 5:
        newlist.append(x)

print(newlist)

user = int(input('select a number: '))
print(a[0:user-1])