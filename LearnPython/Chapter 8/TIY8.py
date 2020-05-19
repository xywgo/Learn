# 8-1.Message:
def display_message():
	print("I am going to learning about Functions in this chapter.")

display_message()


# 8-2.Favorite Book:
def favorite_book(title):
	print(f"One of my favorite books is {title.title()}.")

favorite_book("alice in wonderland")

# 8-3. T-Shirt:
def make_shirt(size, message='I love python'):
	print(f"\n\tSize: {size}\n\tMessage: {message}")

make_shirt('m', "love")
make_shirt(message='follow your heart', size='s')

# 8-4.Large Shirts:
make_shirt('L')

# 8-5. Cities:
def describe_city(city, country='china'):
	print(f"{city.title()} is in {country.title()}")

describe_city('beijing')
describe_city(city='shanghai')
describe_city('new yourk', 'US')

# 8-6. City Names:
def city_country(name, country):
	info = f"{name}, {country}"
	return info

pair1 = city_country('Beijing', country='China')
pair2 = city_country('shanghai', 'China')
pair3 = city_country('New York', "US")

print(pair1)
print(pair2)
print(pair3)

#8-7. Album:
def make_album(artist, title, songs=None):
	if songs:
		album = {'artist': artist, 'title': title, 'songs': songs}
	else:
		album = {'artist': artist, 'title': title}
	return album
album1 = make_album('adele', '17', 12)
print(album1)
album2 = make_album('jason mars', 'we sing, we dance, we jumpe')
print(album2)

# 8-8.User Albums:
# while True:
# 	print("\nPlease tell me some info about the album")
# 	print("(enter 'q' at any time to quit.")
# 	am_artist = input("please tell me the artist name of the album: ")
# 	if am_artist == 'q':
# 		break
# 	am_titile = input("please tell me the title of the album: ")
# 	if am_titile == 'q':
# 		break
# 	am_songs = int(input("How many songs will the album have: "))
# 	if am_songs == 'q':
# 		break
# 	album = make_album(am_artist, am_titile, am_songs)
# 	print(album)
# 8-9.Messages:
def show_messages(messages):
	for message in messages:
		print(message)

short_messages = ['Hello, World!', 'Have a nice day!', 'Happy to see you!']

# 8-10.Sending Messages:
def send_messages(unsent_messages, sent_messages):
	while unsent_messages:
		sent_message = unsent_messages.pop()
		print(f"sent a message:{sent_message}")
		sent_messages.append(sent_message)

sent_messages = []
send_messages(short_messages[:], sent_messages)
show_messages(sent_messages)

# 8-11 Archived Messages:
print(short_messages)

# 8-12. Sandwiches:
def sandwiches(*items):
	print(items)

sandwiches('bread', 'beef')
sandwiches('bread', 'vegatables','pork')
sandwiches('pork')

# 8-13.User Profile:
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('Jason', 'Lee',
	                          faovorite='music',
	                          hate='math')

print(user_profile)

# 8-14.Cars:
def make_cars(manufacturer, model, **cars):
	cars['manufacturer'] = manufacturer
	cars['model'] = model
	return cars
car = make_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8-15. Printing Models:
from printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


