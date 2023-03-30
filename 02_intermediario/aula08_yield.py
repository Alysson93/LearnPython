def generator(n=0, maxi = 10):
	while True:
		yield n
		n += 1
		if n > maxi:
			return

gen = generator(n=0)

for i in gen:
	print(i)