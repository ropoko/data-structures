text = str(input('escreva uma frase: '))

words = (text.split(' '))

for x in (words[::-1]):
    print(x)
