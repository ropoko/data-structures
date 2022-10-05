import datetime

def main():
	hour = datetime.datetime.now().hour

	greeting = ''

	if hour >= 6 and hour <= 12:
		greeting = 'Good Morning!'
	elif hour >= 12  and hour < 18:
		greeting = 'Good Afternoon!'
	elif hour >= 18 and hour <= 23:
		greeting = 'Good Evening!'
	else:
		greeting = 'Good Night!'

	print(f'{hour}h - {greeting}')


if __name__ == '__main__':
	main()
