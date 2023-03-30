from itertools import count, combinations, permutations, product

# count() é um gerador infinito. começa do zero.
# pode ter dois parâmetros: start e step.
# count(10) - começa do 10
# count(10, 2) - começa do 10 e vai de 2 em 2
c1 = count()

pessoas = ['Alysson', 'Pereira', 'Assunção']

camisetas = [
	['preta', 'branca'],
	['P', 'M', 'G'],
	['Masculino', 'Feminino', 'Unissex'],
	['algodão', 'poliéster']
]

# Combinação - ordem não importa
# Neste caso, combina em grupos de 2
comb = combinations(pessoas, 2)
print('Combinação:')
for i in comb:
	print(i)
print()


# Permutação - ordem importa
# Neste caso, permuta em grupos de 3
per = permutations(pessoas, 3)
print('Permutação:')
for i in per:
	print(i)
print()

# product
pro = product(*camisetas)
for i in pro:
	print(i)