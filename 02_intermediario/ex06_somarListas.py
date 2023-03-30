from itertools import zip_longest

def soma_lista(x, y):
	minimo = min(len(x), len(y))
	return [x[i] + y[i] for i in range(minimo)]

par = [0, 2, 4, 6, 8]
impar = [1, 3, 5, 7, 9, 11, 13]

print(soma_lista(par, impar))

# Outra solução:
soma_zip = [x + y for x, y in zip(par, impar)]
print(soma_zip)

# Solução com zip_longest
soma_zip_longest = [x + y for x, y in zip_longest(par, impar, fillvalue=0)]
print(soma_zip_longest)