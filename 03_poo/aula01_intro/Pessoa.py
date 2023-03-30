import json

class Pessoa:

	# Atributos de classe:
	ano_atual = 2023
	qtd = 0

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
		Pessoa.qtd += 1

	def get_ano_nascimento(self):
		return Pessoa.ano_atual - self.idade

	@classmethod
	def numero_de_vagas(cls):
		vagas = 100 - cls.qtd
		if vagas <= 0:
			return 'Não há vagas.'
		else:
			return f'Ainda existem {100 - cls.qtd} vagas.'


dados = {
	'nome': 'Pereira',
	'idade': 30
}

p1 = Pessoa('Alysson', 29)
p2 = Pessoa('Vitória', 11)
p3 = Pessoa(**dados)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(Pessoa.numero_de_vagas())


bd = [vars(p1), vars(p2), vars(p3)]

with open('pessoas.json', 'w') as arquivo:
	json.dump(bd, arquivo, ensure_ascii=False, indent=2)