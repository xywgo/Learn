import  json

filename = 'favorite_number.txt'
favorite_number = input("Please tell me your favorite number: ")
with open(filename, 'w') as f:
	json.dump(favorite_number, f)


