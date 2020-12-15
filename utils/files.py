import os

# Cria um arquivo
file = open('teste.txt', 'x')

# escreve no arquivo
file.write('isso aqui é um teste!')
file.close()

# lê e printa o arquivo
file = open("teste.txt", "r") 
print(file.read())

file.close()

# Verifica se o arquivo existe e se existir, deleta
if os.path.exists("teste.txt"):
  os.remove("teste.txt")
else:
  print('txt já foi Deletado :D')
