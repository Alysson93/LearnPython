class Pessoa:

	def __init__(self, nome, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome

	def falou(self):
		return self.__class__.__name__, 'falou.'