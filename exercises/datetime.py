import datetime

data = datetime.datetime.now()

horaAtual = data.hour

if horaAtual > 6 and horaAtual < 12:
    print('Bom Dia!')
elif horaAtual >= 12  and horaAtual < 18:
    print('Boa Tarde!')
elif horaAtual >= 18 and horaAtual <= 23:
    print('Boa Noite!')
else:
    print('Boa Madruagada!')