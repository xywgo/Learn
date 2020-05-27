
while True:

	try:
		number1 = input("Please enter a number:(enter 'q' to quit) ")
		if number1 == 'q':
			break
		number1 = int(number1)
		number2 = input("Please enter another number:(enter 'q' to quit) ")
		if number2 == 'q':
			break
		number2 = int(number2)
	except ValueError:
		print("You must enter a number")
	else:
		results = number1 + number2
		print(results)