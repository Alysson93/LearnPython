import json

pessoa = {
	'nome': 'Alysson',
	'sobrenome': 'Pereira Assunção',
	'altura': 1.63,
	'dev': True,
	'technologies': ['Python', 'C#', 'JavaScript'],
	'enderecos': [
		{'rua': 'C. Ludugero', 'bairro': 'Cohab 1', 'n': 80},
		{'rua': 'Não lembro', 'bairro': 'Pontilhão', 'n': 84}
	]
}


with open('data.json', 'w', encoding='utf-8') as file:
	# Jogando o objeto no arquivo json:
	json.dump(pessoa, file, ensure_ascii=False, indent=2)


with open('data.json', 'r', encoding='utf-8') as file:
	pessoa = json.load(file)
	print(pessoa)