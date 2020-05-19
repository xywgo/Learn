def get_formatted_name(fisrt_name, last_name):
	"""Display a simple greeting."""
	full_name = f"{fisrt_name} {last_name}"
	return full_name

# This is an infinite loop!
while True:
	print("\nPlease teel me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("Fisrt name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break


	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")
 