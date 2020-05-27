def cats_dogs_names(filename):
	try:
		with open(filename) as f:
			pets_names = f.read()
	except FileNotFoundError:
		pass
	else:
		print(pets_names)
filenames = ['cats.txt', 'pig.txt', 'dogs.txt']


for filename in filenames:
	cats_dogs_names(filename)