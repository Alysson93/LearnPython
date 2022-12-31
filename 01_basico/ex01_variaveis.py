from datetime import date

class Pessoa:

	def __init__(self, nome, sobrenome, ano_de_nascimento, homem, altura, peso):
		self.nome = nome
		self.sobrenome = sobrenome
		self.ano_de_nascimento = ano_de_nascimento
		self.homem = homem
		self.idade = date.today().year - ano_de_nascimento
		self.maior_de_idade = False if self.idade < 18 else True
		self.altura = altura
		self.peso = peso


	def imc(self):
		return self.peso / (self.altura * 2)


##########################

while True:

	try:
		nome = input('Nome: ')
		sobrenome = input('Sobrenome: ')
		ano_de_nascimento = int(input('Ano de nascimento: '))
		sexo = input('Sexo: (1 para masculino, 2 para feminino) ')
		sexo = True if sexo == '1' else False
		altura = float(input('Altura: '))
		peso = float(input('Peso: '))

		p = Pessoa(nome, sobrenome, ano_de_nascimento, sexo, altura, peso)

		print(f'{p.nome} tem {p.idade} anos')
		print(f'IMC: {p.imc():.2f}') if p.maior_de_idade and p.homem else None
		break
	
	except:
		print('Davo inválido. Tente novamente.\n')