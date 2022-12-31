x = input('Número: ')

try:
	x_float = float(x)
	print(f'O dobro de {x} é {x_float * 2:.2f}')
except:
	print('Isto não é um número.')
