with open('guest_book.txt', 'a') as gb:
	while True:
		guest = input("Please enter your name:\n(enter 'q' to quit) \n__")
		if guest == 'q':
			break
		else:
			print(f"Hello {guest}, thanks for your coming.")
			gb.write(guest + "\n")

			