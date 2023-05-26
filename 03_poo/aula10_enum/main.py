import enum

class Direcoes(enum.Enum):
	ESQUERDA = 'Socialismo'
	DIREITA = 'Capitalismo'
	ACIMA = enum.auto()
	ABAIXO = enum.auto()


def mover(direcao: Direcoes) -> None:
	if not isinstance(direcao, Direcoes):
		raise ValueError('Direção não encontrada')
	print(f'Movendo para {direcao.value}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)