def main():
	random_word = str.join(' ', 'apple')

	word = ''

	for x in range(random_word.__len__()):
		word += '_'

	while word.count('_') > 0:
		print("What's the word? ", word)

		letter_try = str(input('try one letter: '))

		if letter_try in random_word:
			index = random_word.index(letter_try)

			aux = list(word) # so we can change the letter by index
			aux[index] = letter_try

			word = str.join('', aux)
			print(word)
		else:
			print('try again!')

if __name__ == '__main__':
	main()
