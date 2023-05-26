from abc import ABC, abstractmethod

class Notificacao(ABC):

	def __init__(self, mensagem) -> None:
		self.mensagem = mensagem


	@abstractmethod
	def enviar(self) -> bool: ...




####################


class Email(Notificacao):

	def enviar(self) -> bool:
		print('Enviando e-mail:', self.mensagem)
		return True



####################


class SMS(Notificacao):

	def enviar(self) -> bool:
		print('Enviando SMS:', self.mensagem)
		return False




####################

def notificar(notificacao: Notificacao):
	notificao_enviada = notificacao.enviar()
	if notificao_enviada:
		print('Notificação enviada')
	else:
		print('Notificação não enviada')



notificar(Email('Olá!'))
notificar(SMS('Tchau!'))