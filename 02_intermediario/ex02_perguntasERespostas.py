perguntas = [
	{
		'pergunta': 'Quanto é 2 + 2?',
		'opcoes': [1, 2, 3, 4],
		'resposta': 4
	},
	{
		'pergunta': 'Quanto é 5 x 5?',
		'opcoes': [25, 20, 24, 10],
		'resposta': 25
	},
	{
		'pergunta': 'Quanto é 10 / 2?',
		'opcoes': [4, 5, 2, 1],
		'resposta': 5
	}
]

acertos = 0

for i in perguntas:

	print(i['pergunta'])

	opcoes = i['opcoes']
	for indice, valor in enumerate(opcoes):
		print(f'{indice}) - {valor}')

	escolha = input('Escolha uma opção: ')

	acertou = False
	escolha_int = None
	qtd_opcoes = len(opcoes)

	if escolha.isdigit():
		escolha_int = int(escolha)

	if escolha_int is not None:
		if escolha_int >= 0 and escolha_int < qtd_opcoes:
			if opcoes[escolha_int] == i['resposta']:
				acertou = True

	if acertou:
		print('Você acertou!')
		acertos += 1
	else:
		print('Você errou.')



print(f'Total de acertos: {acertos}')