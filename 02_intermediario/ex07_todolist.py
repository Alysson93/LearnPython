lista = []
excluidos = []

def verificar(lista):
	if len(lista) == 0:
		return
	return True


def listar(lista):
	print('TAREFAS:')
	for i in lista:
		print(i)


while True:
	print('1- Nova tarefa')
	print('2 - Listar tarefas')
	print('3 - Desfazer tarefa')
	print('4 - Refazer tarefa')
	print('5 - Sair')
	option = input('Digite uma opção: ')
	if option == '1':
		task = input('Digite a terefa: ')
		lista.append(task)
		listar(lista)
	elif option == '2':
		if verificar(lista):
			listar(lista)
		else:
			print('Nada a listar.')
	elif option == '3':
		if verificar(lista):
			task = lista.pop()
			excluidos.append(task)
			listar(lista)
		else:
			print('Nada a desfazer.')
	elif option == '4':
		if verificar(excluidos):
			task = excluidos.pop()
			lista.append(task)
			listar(lista)
		else:
			print('Nada a refazer.')
	elif option == '5':
		print('Até a próxima!')
		break
	else:
		print('Opção inválida. Digite un número entre 1 e 5.')
	print()