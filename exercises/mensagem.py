name = str(input('Your name: '))  
age = int(input('How old are you? '))

msg = '{}, in 100 years, you will have {} years!'
print(msg.format(name, str(age+100)))