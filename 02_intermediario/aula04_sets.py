s1 = set()

s1.add('Alysson')

s1.add(1)

# Para mandar vários valores, usar iterável
s1.update(('Olá mundo', 1, 2, 3, 4))

s1.discard(2)

print(s1)

#######################

s2 = {1, 2, 3}

s3 = {2, 3, 4}

# União de sets
print(s2 | s3) # 1, 2, 3, 4

# Intersecção de sets
print(s2 & s3) # 2, 3

# Diferença (Remove elementos de um que também estão no outro)
print(s2 - s3) # 1

# Diferça simétrica (elementos únicos)
print(s2 ^ s3) # 1, 4