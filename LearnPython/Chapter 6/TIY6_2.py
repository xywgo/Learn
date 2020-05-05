print("6-7.People")
person_0 = {
	'first_name': 'alex',
	'last_name': 'cooper',
	'age': 18,
	'city': 'new york'
}
person_1 = {
	'first_name': 'vecent',
	'last_name': 'green',
	'age': 9,
	'city': 'beijing'
}
person_2 = {
	'first_name': 'jack',
	'last_name': 'cott',
	'age': 19,
	'city': 'London'

}

people = [person_0, person_1, person_2]

for person in people:
	print(f"\nFull name: {person['first_name'].title()} {person['last_name'].title()}"
		f"\n\tAge: {person['age']}\n\tCity: {person['city'].title()}")

print("\n6-8.Pets")
pet_0 = {
	'name': "coco",
	'kind': 'cat',
	'owner': 'lily',
}
pet_1 = {
	'name': 'lucky',
	'kind': 'dog',
	'owner': 'jason',

}
pet_2 = {
	'name': 'dodo',
	'kind': 'dog',
	'owner': 'tom',
}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
	print(f"\n{pet['owner'].title()} has a {pet['kind']} named, {pet['name'].title()}.")


print("\n6-9. Favorite Places")
favorite_places = {
	'lala': ['new york', 'beijing', 'guangzhou'],
	'emily': ['LA', 'huangshan', ],
	'susan': ['suzhou', 'xi\'an', 'chengdu']
}
for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")

	for place in places:
		print(f"\t{place.title()}")

print("6-10. Favorite Numbers:")
favorite_numbers = {
	'maya': [7, 8,],
	'lily': [10, 12,],
	'jodi': [13,],
	'vecent': [8, 9, 11,],
}

for name, numbers in favorite_numbers.items():
	if len(numbers) == 1:
		print(f"\n{name.title()}'s favorite number is {numbers[0]}.")
	else:
		print(f"\n{name.title()}'s favorite numbers are:")

		for number in numbers:
			print(f"\t{number}")

print("\n6-11. Cities:")
cities = {
	'beijing': {
	'country': 'China',
	'population': '2153.6 million',
	'fact': 'Capital of China',
	},
	'shanghai': {
	'country': 'China',
	'population': '2428.14 million',
	'fact': 'largest city of China',
	},
	'london': {
	'country': 'UK',
	'population': '890 million',
	'fact': 'Capital of UK',
	},
}

for city, city_info in cities.items():
	print(f"\n\tCity: {city.title()}")
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']
	print(f"\tCountry: {country}")
	print(f"\tPoulation: {population}")
	print(f"\tFact: {fact}")

print("\n6-12. Extensions:")
