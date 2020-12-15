from sys import exit

num = int(input('Insert a number: '))

for x in range(2, num - 1):
	if num % x == 0:
		print("not prime.")
		exit(0)
	elif num % x != 0:
		continue
	elif num == 0:
		print("not prime.")
		exit(0)
	elif num < 0:
		print("not prime.")
		exit(0)
print('prime')