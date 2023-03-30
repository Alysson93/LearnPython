pessoa = {
	'nome': 'Alysson',
	'idade': 29,
	'sexo': 'M',
	'emails': [
		'alyssondev93@outlook.com', 
		'apa1@discente.ifpe.edu.br'
	]
}

# Criar uma nova chave ou editar  - sinal de atribuição
pessoa['telefone'] = '982858952'

# Deletar chave
del pessoa['telefone']

print(tuple(pessoa.keys()))
print(tuple(pessoa.values()))

print(pessoa.get('telefone'))
emails = pessoa.pop('emails')
print(emails)
pessoa.update(nome = 'Pereira', idade = 30)
print(pessoa)