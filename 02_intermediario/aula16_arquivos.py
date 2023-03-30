import os

arquivo = 'arquivo.txt'

# r - leitura de arquivos

# w - (apaga antes) escrita de arquivos, w+ escrita e leitura

# x -criação de arquvios

# a - escreve no final

with open(arquivo, 'a+', encoding='utf-8') as file:
	file.write('Linha 1\n')
	file.write('Linha 2\n')
	file.writelines(
		('Linha 3\n', 'Linha 4\n', 'Linha 5\n')
	)
	file.seek(0,0) # Voltar ao topo do arquivo
	# print(file.read())
	# print(file.readline())
	for line in file.readlines():
		print(line.strip())


os.rename(arquivo, 'new.txt')

os.unlink(arquivo) # Ou os.remove() apaga o arquivo