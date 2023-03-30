digitos = [x for x in range(10)]

produtos = [
	{'nome': 'p1', 'preco': 20},
	{'nome': 'p2', 'preco': 25},
	{'nome': 'p3', 'preco': 30},
	{'nome': 'p4', 'preco': 40}
]

impares = ['x' if x % 2 == 0 else x for x in digitos]
print(impares)



######## Mapear dados
dobro = [x * 2 for x in digitos]
print(dobro)


######## Filtrar dados
pares = [x for x in digitos if x % 2 == 0]
print(pares)


######## Mapear e filtrar dados
novos_produtos = [
	{**produto, 'preco': produto['preco'] * 1.05}
	if produto['preco'] > 25
	else
	{**produto}
	for produto in produtos
	if produto['preco'] < 40
]
print(novos_produtos)

if False:
	mapfilter = [x if True else y for x in range(10) if x % 2 == 0]



## Também é possível fazer compressão de dicionários:

pessoa = {
	'nome': 'alysson',
	'idade': 29,
	'sexo': 'm'
}

dc = {
	chave: valor.capitalize()
	if isinstance(valor, str) else valor
	for chave, valor in pessoa.items()
}
print(dc)


## Não existe compressão de tuplas.
## Existe porém, generators.

generator = (n*2 for n in range(1,11))
print(next(generator))