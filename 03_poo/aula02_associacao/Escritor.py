class Escritor:

	def __init__(self, nome):
		self.nome = nome
		self._ferramenta = None

	@property
	def ferramenta(self):
		return self._ferramenta

	@ferramenta.setter
	def ferramenta(self, ferramenta):
		self._ferramenta = ferramenta
	