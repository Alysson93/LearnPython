lista = [
	
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	[9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
	[1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
	[0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
]


######## Minha solução:

for i in lista:
	lista_vazia = set()
	for j in i:
		if j in lista_vazia:
			print(j)
			break
		else:
			lista_vazia.add(j)
	if list(lista_vazia) == i:
		print(-1)