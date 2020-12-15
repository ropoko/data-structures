lista = ["a", 'a', "b", 'b',"a", "c", "c"]

# Convert to Dictionary, because Dictionarys cannot have duplicates.
lista = list(dict.fromkeys(lista))

# Then, convert back to list.
print(lista)