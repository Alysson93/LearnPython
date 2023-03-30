pessoa = {
	'nome': 'Alysson',
	'sobrenome': 'Pereira'
}


# Desempacotando
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2, b1, b2)


# Empacotando
pessoa_completa = {**pessoa, 'idade': 29}
print(pessoa_completa)