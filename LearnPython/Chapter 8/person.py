def build_person(fisrt_name, last_name, age=None):
	"""Return a dictionary of information about a person."""
	person = {'first': fisrt_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)