def validar_cpf(x):

	for cont in range(10, 12):

		digito = 0

		for i in x:
			digito += cont * int(i)
			cont -= 1

		digito *= 10

		digito %= 11

		digito = 0 if digito > 9 else digito

		digito = str(digito)

		x += digito

	return x
