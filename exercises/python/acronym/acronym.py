from os import path, getcwd

def main():
	phrase = str(input('Tell me your thoughts: '))

	letters = [word[0].upper() for word in phrase.split(' ')]

	for x in letters:
		get_word(x)


def get_word(letter: str):
	word_list_file = path.realpath(
		path.join(getcwd(), path.dirname(__file__), 'word_list.txt')
	)

	with open(word_list_file, 'r') as file:
		for word in file:
			if word[0].upper() == letter:
				print(f'{letter} -> {word}')


if __name__ == '__main__':
	main()
