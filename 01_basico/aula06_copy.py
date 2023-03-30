import copy

nome = 'Alysson'

novo = nome

nome = 'Pereira'

print(novo, nome)

print('========================')

# Com dados mutáveis, a cópia não ocorre da mesma forma.
# As duas variáveis apontam para o mesmo endereço.

lista = ['Aliçu', 'Pereira', 'Assunção']

falsa_lista_nova = lista

falsa_lista_nova[0] = 'Alysson'

print(lista)

print('========================')

# Para ter uma nova lista baseada em outra,
# pode-se usar o método copy (para lista de valores imutáveis).

lista_nova = lista.copy()

lista_nova[0] = 'Alison'

print(lista, lista_nova)

print('========================')


# Com dados mutáveis, deve-se usar uma deep copy.

pessoa = {
	'nome': 'Alysson',
	'idade': 28,
	'emails': [
		'apa1@discente.ifpe.edu.br',
		'alyssondev93@outlook.com.br'
	]
}

nova_pessoa = copy.deepcopy(pessoa)

nova_pessoa['emails'] = 'No emails'

print(pessoa)
print(nova_pessoa)