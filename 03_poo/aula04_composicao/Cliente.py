from Endereco import Endereco

class Cliente:

	def __init__(self, nome):
		self.nome = nome
		self.enderecos = []
	
	def inserir_enderecos(self, rua, numero):
		self.enderecos.append(Endereco(rua, numero))

	def listar_enderecos(self):
		for i in self.enderecos:
			print(i.rua, i.numero)