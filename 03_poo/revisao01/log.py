from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / 'log.txt'

# Abstração

class Log(ABC):

	@abstractmethod
	def _log(self, msg): ...


	def log_error(self, msg):
		return self._log(f'Erro em {self.__class__.__name__}: {msg}')


	def log_success(self, msg):
		return self._log(f'Sucesso! {self.__class__.__name__}: {msg}')




##########

class LogFileMixin(Log):

	def _log(self, msg):
		msg_format = f'{msg} ({self.__class__.__name__})'
		with open(LOG_FILE, 'a') as file:
			file.write(msg_format)
			file.write('\n')



##########

class LogPrintMixin(Log):

	def _log(self, msg):
		print(msg)



##########

if __name__ == '__main__':
	lf = LogFileMixin()
	lf.log_error('Qualquer coisa')
	lf.log_success('Parabéns!')
	lp = LogPrintMixin()
	lp.log_error('Qualquer coisa')
	lp.log_success('Parabéns!')