from functools import reduce

produtos = [
	{'nome': 'p1', 'preco': 99},
	{'nome': 'p1', 'preco': 100},
	{'nome': 'p1', 'preco': 50},
	{'nome': 'p1', 'preco': 200},
]

dobro = map(
	lambda p: p['preco'] * 2,
	produtos
)

maiores = filter(
	lambda p: p['preco'] > 10,
	produtos
)

valor_total = reduce(
	lambda acumulador, produto: acumulador + produto['preco'],
	produtos,
	0
)

for i in dobro:
	print(i)
print()

for i in maiores:
	print(i)
print()

print(valor_total)