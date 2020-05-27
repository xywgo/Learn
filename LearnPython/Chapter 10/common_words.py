def count_word(filename, words):
	"""Count certain word or phrase apper times in in a txt file"""
	with open(filename) as f:
		content = f.read()

	times = content.lower().count(words)
	return times


times_the = count_word('little_women.txt', 'the')
print(times_the)


times_then = count_word('little_women.txt', 'then')
print(times_then)