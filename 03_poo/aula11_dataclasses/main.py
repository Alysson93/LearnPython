from dataclasses import dataclass

@dataclass
class Pessoa:
	nome: str
	idade: int

	def __post_init__(self):
		

	def frase(self):
		return f'{self.nome} tem {self.idade} anos.'



p1 = Pessoa('Alysson', 29)
p2 = Pessoa('Pereira', 28)

print(p1 == p2)
print(p1.frase())