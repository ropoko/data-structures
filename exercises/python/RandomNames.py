import random

def Converter(name, seperator):
    strFinal = seperator.join(name)
    return strFinal

def GeneratorNames():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '01234567889'

    letters = random.choices(alphabet, k=2)
    number = random.choices(numbers, k=3)

    name = list(letters + number)

    print('Your robot name: ' + Converter(name, ''))
    print("Want another name? Y/N")

    user = str(input()).lower()

    if user.__eq__('y'):
        GeneratorNames()
    else:
        print('GoodBye!')

GeneratorNames()