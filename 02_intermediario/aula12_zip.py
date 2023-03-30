from itertools import zip_longest

def zipper(l1, l2):
	minimo = min(len(l1), len(l2))
	return [(l1[i], l2[i]) for i in range(minimo)]



cidades = ['Belo Jardim', 'Ceará', 'Belo Horizonte']

estados = ['PE', 'FT', 'BH', 'BA']

print(zipper(cidades, estados))
print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados)))