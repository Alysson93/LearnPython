# Os argumentos vem como uma tupla
def mult(*args):
	total = 1
	for i in args:
		if i == 0:
			return 0
		total *= i
	return total


resultado = mult(1, 2, 3, 4, 5)

print(resultado)
