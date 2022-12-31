nomes = ['Alysson', 'Pereira', 'Assunção']

# O enumerate cria um iterador com tuplas índice / valor 

for i in enumerate(nomes):
	print(i)


# or

for indice, valor in enumerate(nomes):
	print(indice, valor)