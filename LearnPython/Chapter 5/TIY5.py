# 5-1. Conditional Test:
car = 'subaru'

print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I prdict Flase")
print(car == 'audi')


weather = 'rain'

print("Is weather == 'rain'? I predict True.")
print(weather == 'rain')

print("\nIs weather == 'sun'? I predict Flase.")
print(weather == 'sun')


name = 'Jason'

print("Is your name == 'Jason'? I predict True.")
print(name == 'Jason')

print("\nIs your name == 'jason'? I predict True")
print(name.lower() == 'jason')


# 5-2. More Conditinal Test:

numbers = list(range(0,10))
print(numbers)

if numbers[2] != 1:
	print(f"\n{numbers[2]} != 1")
	print(numbers != 1)

print(f"\n{numbers[3]} >= {numbers[4]} ")
print(numbers[3] >= numbers[4])

print(f"\n{numbers[3]} < {numbers[4]}")
print(numbers[3] < numbers[4])

tom_likes = ['dog', 'music', 'book']

print("does tom like dog and book?")
print('dog' in tom_likes and 'book' in tom_likes)

print('Does Tom like music or book?')
print('music' in tom_likes or 'book' in tom_likes)

print('Does Tom like cat?')
print('cat' in tom_likes)

print("so Tom don't like cat ?")
print('cat' not in tom_likes)

# 5-3&4&5. Alien Colors #1&2&5:
alien_color = 'green' 
if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 15
print(f"\nYour earned {points} points")


print("\n5-6. Stages of Life:")
age = 18

if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'kid'
elif age < 20:
	stage = 'teenager'
elif age < 65:
	stage = 'adult'
else:
	stage = 'elder'
print(f"your are a(n) {stage}.")

print("\n5-7. Favorite Fruit")
favorite_fruits = ['apple', 'mango', 'pineapple', 'banana']
if 'apple' in favorite_fruits:
	print("You really like apple")
if 'mango' in favorite_fruits:
	print("You really like mango")
if 'pineapple' in favorite_fruits:
	print("You really like pineapple")
if 'orange' in favorite_fruits:
	print("You really like orange")
if 'banana' in favorite_fruits:
	print("You really like banana")

print("\n5-8. Hello Admin".upper())

usernames= ['admin', 'lucky', 'sunny', 'whish', 'lala']

for username in usernames:
	if username == 'admin':
		print(f"Hello {username}, would you like to see a status report?")
	else:
		print(f"Hello {username}, thank you for logging in again.")

print("\n 5-9. No Users")
usernames = []
if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"Hello {username}, would you like to see a status report?")
		else:
			print(f"Hello {username}, thank you for logging in again.")
else:
	print("We need to find some users!")

print("\n5-10. Checking usernames:")

current_users = ['admin', 'lucky', 'sunny', 'whish', 'lala']
new_users = ['tek', 'lucky', 'wuby','saga', 'Lala']

for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"{new_user} has been used,please enter a new username")
	else:
		print(f"Hi {new_user}, this is available username.")

print("5-11. Ordinal Numbers:")

ordinal_numbers = list(range(1,10))
for ordinal_number in ordinal_numbers:
	if ordinal_number == 1:
		print(f"\n\t{ordinal_number}st")
	elif ordinal_number == 2:
		print(f"\n\t{ordinal_number}nd")
	else:
		print(f"\n\t{ordinal_number}th")

print("\n5-12. Styling if statement:")
print("\n5-13. Your Ideas")


