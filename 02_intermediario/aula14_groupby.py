from itertools import groupby

boletim = [
	
	{'nome': 'Alysson', 'nota': 'A'},
	{'nome': 'Pereira', 'nota': 'B'},
	{'nome': 'Assunção', 'nota': 'A'},
	{'nome': 'Vitória', 'nota': 'C'},
	{'nome': 'Anderson', 'nota': 'B'},
	{'nome': 'Jordy', 'nota': 'C'},

]

notas = lambda item: item['nota']

# Primeiro passo: ordenar
boletim.sort(key = notas)

# Segundo passo: agrupar por notas
grupos = groupby(boletim, notas)

for chave, grupo in grupos:
	print(chave)
	for aluno in grupo:
		print(aluno)
	print()

