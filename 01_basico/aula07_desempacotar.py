# Desempacotando...

nomes = ['Alysson', 'Pereira', 'Assunção']

idades = [29, 30, 31]

a, b, c = idades

nome, *sobrenome = nomes

# caso não queira usar uma variável:
# nome, *_ = nomes
# O _ é uma variável que convém não usar.

print(a, b, c)

print(nome, sobrenome)
