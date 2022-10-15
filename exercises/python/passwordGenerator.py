import random

Useroption = str(input('Weak, Medium or Strong password? ').lower())
passlen = int(input('escolha a quantidade de caracteres: '))


weak = 'abcdefghijklmnopqrstuvwxyz01234567890'
medium = 'abcdefghijklmnopqrstuvwxyz01234567890!@#$BCDEFG'
strong = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?][}{'

if Useroption == 'weak':
    p =  "".join(random.sample(weak, passlen))
elif Useroption == 'medium':  
    p =  "".join(random.sample(medium, passlen))
else:
    p =  "".join(random.sample(strong, passlen))

print('Sua Senha: ', p)
