# LIsta com nomes de carros
carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Mustang", "Palio", "Corsa", "Fusca"]

# Varíavel para iterar a lista carros
itCarros = iter(carros)

# Enquanto for verdadeiro
while True:

	# Tentar mostrar tudo
	try:

		# Mostrar
		print(next(itCarros))

	# Se aparecer erro de StopIteration
	except StopIteration:

		# Mostrar que acabou
		print("\nFim da lista")

		# Parar o looping while
		break
