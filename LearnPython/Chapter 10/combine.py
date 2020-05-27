import  json

filename = 'favorite_number.txt'
try:
	with open(filename) as f:
		favorite_number = json.load(f)
except FileNotFoundError:
	with open(filename, 'w') as f:
		favorite_number = input("Please enter your favorite number: ")
		json.dump(favorite_number, f)
		print(f"We will remember your favorite number")
else:
	print(f"I know your favorite number! It's {favorite_number}.")

