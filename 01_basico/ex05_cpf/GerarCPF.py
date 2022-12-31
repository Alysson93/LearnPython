import random
from ValidarCPF import validar_cpf

cpf = ''

for i in range(9):
	cpf += str(random.randint(0, 9))

cpf = validar_cpf(cpf)

print(cpf)