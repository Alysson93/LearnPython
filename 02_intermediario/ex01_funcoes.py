def duplicar(x):
	return x * 2

def triplicar(x):
	return x * 3

def quadruplicar(x):
	return x * 4


# E se eu não quiser criar várias funções?

def criar_multiplicador(multiplicador):
	def multiplicar(x):
		return x * multiplicador
	return multiplicar

duplica = criar_multiplicador(2)

print(duplica(5))