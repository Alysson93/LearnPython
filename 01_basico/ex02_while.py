frase = 'O Python é uma linguagem multiparadigma. ' \
	'Estou aprendendo a desenvolver projetos em Python.'


# O count conta o número de ocorrências de um elemento em uma str
#print(frase.count('Python')) # Retorna 2

i = 0

qtd_aparece_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):

	letra_atual = frase[i]

	if letra_atual == ' ':
		i += 1
		continue

	quantas_vezes_letra_apareceu = frase.count(letra_atual)
	
	if qtd_aparece_mais_vezes < quantas_vezes_letra_apareceu:
		qtd_aparece_mais_vezes = quantas_vezes_letra_apareceu
		letra_que_apareceu_mais_vezes = letra_atual

	i += 1

print('Letra que apareceu mais vezes:', letra_que_apareceu_mais_vezes)
print('Quantidade:', qtd_aparece_mais_vezes)
