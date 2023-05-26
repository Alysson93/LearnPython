class MyError(Exception):
	...


class AnotherError(Exception):
	...


def levantar():
	exception_ = MyError('A mensagem do meu erro', 	'abc', 'Full Body')
	raise exception_


try:
	levantar()
except (MyError, ZeroDivisionError) as error:
	print(error.__class__,__name__)
	print(error)
	exception_ = AnotherError('Vou lançar de novo')
	raise exception_ from error