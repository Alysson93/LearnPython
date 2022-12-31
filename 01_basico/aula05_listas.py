primos = [2, 3, 5, 7, 11]

# É interessante evitar mover elementos da lista,
# pois isto exige muito processamento.
# O ideal é manipular elementos do fim da lista.

# create
# append - ao final da lista
primos.append(13)
print(primos)

# insert - em um índice específico, levando outros índices para frente.
primos.insert(2, 17)
print(primos)

# read
print(primos)

# update
primos[4] = 2
print(primos)

# delete
del primos[0]
print(primos)

# pop - remove e retorna o último elemento da lista por padrão.
x = primos.pop()
print(primos, x)
# O pop também remove específicos.
# Ex: primos.pop(2)