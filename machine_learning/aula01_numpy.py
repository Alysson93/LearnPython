import numpy as np

# Construindo um array (lista onde elementos devem ser do mesmo tipo)
a = np.array([1,2,3])
print(type(a), a)
print()

matriz = np.array([(0, 1), (2, 3), (4, 5)])
print(type(matriz), matriz)
print('Maior elemento da matriz:', matriz.max())
print('Menor elemento da matriz:', matriz.min())
print('Soma dos elementos da matriz:', matriz.sum())
print('Média dos elementos da matriz:', matriz.mean())
print('Desvio padrão:', matriz.std())
print()

print('Matriz de zeros:')
print(np.zeros((4,3)))
print()

print('Matriz de uns:')
print(np.ones((2,5)))
print()

print('Matriz identidade')
print(np.eye(3))
print()

print('Numpy version:', np.__version__)