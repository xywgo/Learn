import json


# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	"""prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username,f)
	print(f"We'll remeber you when you come back, {username}")
	return username

def verify_user(username):
	"""Verity if it's a correct user"""
	verify = input(f"if {username} is your username(yes/not): ")
	if verify == 'yes':
		pass
	elif verify == 'not':
		username = get_new_username()
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		username = verify_user(username)
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
	


greet_user()



