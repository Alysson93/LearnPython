try:
	dividendo = int(input('Dividendo: '))
	divisor = int(input('Divisor: '))
	print(dividendo / divisor)
#except NameError:
#	print('Um valor não foi definido')
except ValueError as error:
	print('O valor não corresponde a um inteiro.')
except ZeroDivisionError:
	print('Erro: tentou dividir por zero.')