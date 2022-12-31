import os

palavra = 'macarrão'
tentativas = 0
letras = ''

while True:

	tentativas += 1

	letra = input('Digite uma letra: ')
	if len(letra) != 1:
		print('Você deve digitar uma letra!')
		continue

	if letra in palavra:
		letras += letra


	status = ''
	for i in palavra:
		if i in letras:
			status += i
		else:
			status += '*'

	print(status)

	if status == palavra:
		break

os.system('clear')
print('Fim do jogo.\nNúmero de tentativas:', tentativas)