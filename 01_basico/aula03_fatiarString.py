nome = 'Alysson Pereira Assunção'

print('Nome completo:',nome)
print('Primeiro nome:',nome[:7])
print('Último nome:',nome[16:]) # ou nome[-8:0]
print('Tirando apenas a última letra:',nome[:-1])
print(f'Seu nome invertido é {nome[::-1]}')
print('Pulando de dois em dois:',nome[::2])
if ' ' in nome:
	print('Seu nome tem espaços')
else:
	print('Seu nome não tem espaços.')