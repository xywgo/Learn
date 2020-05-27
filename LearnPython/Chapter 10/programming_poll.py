with open('programming_poll.txt', 'a') as pp:
	while True:
		name = input("Please enter your name(enter 'q' to quit): ")
		responses = input("Why do you like programming?(enter 'q' to quit):\n")
		if name == 'q':
			break
		elif responses == 'q':
			break
		else:
			pp.write(name + "'s responses:\n")
			pp.write(responses + '\n')

