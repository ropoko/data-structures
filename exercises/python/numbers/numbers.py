def main():
	try:
		number = int(input('Please type a decimal number to convert: '))

		octal = oct(number)
		hexa = hex(number)
		binary = bin(number)

		print(f'Binary: {binary}')
		print(f'Octal: {octal}')
		print(f'Hex: {hexa}')

	except ValueError:
		print('\nBAD RESPONSE: you should type a number in base 10 (decimal)')

if __name__ == '__main__':
	main()
