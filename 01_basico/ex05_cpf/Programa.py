import re
from ValidarCPF import validar_cpf

cpf = input("Digite o CPF: ")

cpf = re.sub(r'[^0-9]', '', cpf)

x = cpf[:9]

x = validar_cpf(x)

if x == cpf and cpf[0]*11 != cpf:
	print('CPF Válido')
else:
	print('CPF Inválido')
