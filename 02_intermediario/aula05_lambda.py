lista = [
	{'nome': 'Alysson', 'idade': 29},
	{'nome': 'Pereira', 'idade': 11},
	{'nome': 'Assunção', 'idade': 24}
]

lista.sort(key=lambda item: item['nome'], reverse=True)

for item in lista:
	print(item)