#palindrome = palavras que não mudam mesmo de trás para frente

user = input('Give me a word: ')

tamanho = len(user)

if user[::tamanho] == user[::-tamanho]:
    print('Its Palindrome!')
else:
    print("It isn't  Palindrome!")
