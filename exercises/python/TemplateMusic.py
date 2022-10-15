user = str(input('write a drink name: '))

for i in range(100, 0, -1):
    text = '{} bottles of {} on the wall, {} bottles of {}.'
    print(text.format(i, user, i, user))
    text2 = 'Take one down and pass it around, {} bottles of {} on the wall'
    i-=1
    print(text2.format(i, user))
    print('')
