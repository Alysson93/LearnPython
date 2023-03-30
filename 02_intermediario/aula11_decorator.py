def criar_funcao(funcao):
	def interna(*args, **kwargs):
		print('Decorando...')
		for arg in args:
			is_string(arg)
		resultado = funcao(*args, **kwargs)
		print(resultado)
		print('Decorado.')
		return resultado
	return interna

@criar_funcao
def inverte_string(s):
	return s[::-1]

def is_string(param):
	if not isinstance(param, str):
		raise TypeError('Parâmetro deve ser string')


invertida = inverte_string('123')
print(invertida)