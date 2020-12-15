import re

user = str(input('Write a phrase: '))

regex = "[A-Z]+['a-z]*|['a-z]+"
print(''.join(user[0].upper() for user in re.findall(regex, user)))