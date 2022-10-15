import random

opcoes = ['pedra', 'papel', 'tesoura']

print(opcoes)

while True:

    user = str(input('Escolha: ')).lower()
    machine = random.choice(opcoes)

    print('machine: ', machine)

    if user == machine:
        print('Empate!')
    elif user == 'pedra' and machine == 'papel':
        print('Machine Wins!')
    elif user == 'papel' and machine == 'tesoura':
        print('Machine Wins!')
    elif user == 'tesoura' and machine == 'pedra':
        print('Machine Wins!')

    elif user == 'pedra' and machine == 'tesoura':
        print('You Wins!')
    elif user == 'papel' and machine == 'pedra':
        print('You Wins!')
    elif user == 'tesoura' and machine == 'papel':
        print('You Wins!')

    if str(input('Play again? Y/N\n')).upper() == 'Y':
        continue
    else:
        print('GoodBye!')
        break
