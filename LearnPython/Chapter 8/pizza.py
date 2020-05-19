def make_pizza(size, *toppings):
	"""Print the list of topings that have been requested."""
	print(f"\nMaking a {size} pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
