print("6-1. Person:")
person = {
	'first_name': 'alex',
	'last_name': 'cooper',
	'age': 18,
	'city': 'new york'
}
print(person)

print("\n6-2. Favorite Numbers:")
favorite_numbers = {
	'maya': 7,
	'lily': 10,
	'jodi': 13,
	'vecent': 8,
}
print(favorite_numbers)
favorite_numbers['haley'] = 9
print(f"\nHaley favorite number is : {favorite_numbers['haley']}.")


print("\n6-3. Glossary:")
glossary = {
	'python': 'a program language',
	'string': 'some text wrapped in quote \'\' or double quotes \"\".',
	'list': 'some data separated by commas wrapped in square bracket[].',
	'dictionary': 'some key-values pairs separated by commas  wrapped in braces {}.'
}

for key in glossary:
	print(f"\n{key.title()}: {glossary[key]}")

print("\n6-4. Glossary 2:")
glossary['set'] = 'some data separated by commas but wrapped in braces {}'
glossary['loop through'] = 'to process each element of a list of things'
glossary['slice'] = ' a feature that enables accessing parts of sequences like strings, tuples, and lists'
glossary['sort'] = 'sorts the elements of a given list'
glossary['stdout'] = 'print messages on the screen'

for key in glossary:
	print(f"\n{key.title()}: {glossary[key]}")

print("\n6-5.Rivers:")
rivers = {
	'nile': 'egypt',
	'yellow river': 'china',
	'mississippi': 'us',
}
for name, country in rivers.items():
	print(f"The {name.title()} runs through {country.title()}.")
print("\nThere are some important rivers in the world, they are:")
for name in rivers.keys():
	print(f"\t{name.title()}.")
print("These rivers located in the country of below:")
for country in rivers.values():
	print(f"\t{country.title()}")

print("\n6-6 Polling:")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
poll_names = ['jason', 'phil', 'sarah', 'neo']

for poll_name in poll_names:
	if poll_name not in favorite_languages.keys():
		print(f"Hello {poll_name.title()}, Could you take a poll ?")
	else:
		print(f"Hello {poll_name.title()}, thank you for responding.")

