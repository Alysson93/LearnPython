class Carrinho:

	def __init__( self):
		self._produtos = []

	def total(self):
		return sum([p.preco for p in self._produtos])

	def inserir_produtos(self, *produtos):
		for produto in produtos:
			self._produtos.append(produto)

	def listar_produtos(self):
		print()
		for produto in self._produtos:
			print(produto.nome, produto.preco)

