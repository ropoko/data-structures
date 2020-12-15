def Hex(number):
    return hex(number)

def Binary(number):
    return bin(number)

def Octal(number):
    return oct(number)

number = int(input('Please type a DECIMAL number to convert: '))

if str(number).isnumeric:

    int(number)

    hexa = Hex(number)
    binary = Binary(number)
    octa = Octal(number)

    print('Hex: ' + str(hexa)[2:])
    print('-------=-------')

    print('Binary: ' + str(binary)[2:])
    print('-------=-------')

    print('Octal: ' + str(octa)[2:])
else:
    print('Type a number!')
