word = str(input('Word: '))

answer = word

for x in word:
    word = word.replace(x, '_')

print(' '.join(word))

tries = str(input('Letter: '))

if tries in answer:
    print('Correct!')
else:  
    print('Bad Lucky!')