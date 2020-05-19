def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print(f"\nI Have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('haster', 'harry')
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='lala')


