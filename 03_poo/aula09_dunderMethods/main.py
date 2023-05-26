class Ponto:

	def __init__(self, x, y):
		self.x = x
		self.y = y


	# Definir representação da classe
	# def __str__(self):
	#	return f'{self.x}, {self.y}'


	# Definir representação da classe
	# Usado caso não exista __str__
	# Mais usado para desenvolvedores
	def __repr__(self):
		class_name = type(self).__name__
		return f'{class_name}(x = {self.x!r}, y = {self.y!r})'


	def __add__(self, other):
		novo_x = self.x + other.x
		novo_y = self.y + other.y
		return Ponto(novo_x, novo_y)


	def __gt__(self, other):
		resultado_self = self.x + self.y
		resultado_other = other.x + other.y
		return resultado_self > resultado_other


p = Ponto(1,'alysson')
print(p)

p1 = Ponto(2, 4)
p2 = Ponto(1, 3)
print(p1 + p2)
print(p1 > p2)
print(p1 < p2)