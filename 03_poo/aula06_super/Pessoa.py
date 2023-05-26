class Pessoa:

	def __init__(self, nome):
		self.nome = nome


class Habilidade:
	def __init__(self, poder):
		self.poder = poder

	def liberar(self):
		return 'liberou poder'


class Professor(Pessoa, Habilidade):

	def __init__(self, nome, poder, disciplina):
		super().__init__(nome)
		self.poder = poder
		self.disciplina = disciplina



cliente = Professor('Alysson', 'kamehameha', 'História')
print(cliente.nome,'-' ,cliente.disciplina)
print(cliente.liberar())