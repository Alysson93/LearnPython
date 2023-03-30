def erro_nao_aceito_zero(d):
	if d == 0:
		raise ZeroDivisionError('O valor não pode ser zero.')
	return True

def deve_ser_int_ou_float(x):
	if not isinstance(x, (float, int)):
		raise TypeError(f'{x} deve ser int ou float')


def divisao(x, y):
	deve_ser_int_ou_float(x)
	deve_ser_int_ou_float(y)
	erro_nao_aceito_zero(y)
	return x / y


print(divisao(8, '0'))