def saudacao(msg, name):
	return f'{msg}, {name}!'


#Ao passar com asterisco, vai como valores, não como tupla
def executa(funcao, *args):
	return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Alysson'))


######


def mensagem(saudacao, nome):
	def ola():
		return f'{saudacao}, {nome}!'
	return ola


var = mensagem('Olá', 'Mundo')

print(type(var))
print(var())