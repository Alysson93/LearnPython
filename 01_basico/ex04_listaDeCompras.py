lista = []

while True:
	print('Selecione uma opção:')
	op = input('[i]inserir [l]listar [a]apagar [s]sair: ')
	if op.lower() == 'i':
		valor = input('Item: ')
		lista.append(valor)
	elif op.lower() == 'l':
		if len(lista) < 1:
			print('Nada para listar')
		else:
			for indice, valor in enumerate(lista):
				print(indice, ':' ,valor)
	elif op.lower() == 'a':
		indice = input('Qual o índice do item que você quer apagar? ')
		try:
			del lista[int(indice)]
		except ValueError:
			print('Por favor, digite números inteiros.')
		except IndexError:
			print('Este índice não existe na lista.')
		except Exception:
			print('Ocorreu um erro desconhecido')
	elif op.lower() == 's':
		print('bye!')
		break
	else:
		print('Opção inválida.')