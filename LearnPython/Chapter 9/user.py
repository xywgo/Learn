# 9-3 Users:
class User:
	"""A user model class"""
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		# 9-5
		self.login_attempts = 0

	def describe_user(self):
		print(f"User info: {self.first_name} {self.last_name}.")

	def greet_user(self):
		print(f"Hello, {self.first_name} {self.last_name}")

	# 9-5
	def increment_login_attempts(self):
		"""count user's login apttempts"""
		self.login_attempts += 1
		print(f"You have login {self.login_attempts} times")

	def reset_login_attempts(self):
		"""Reset login attempts to 0"""
		self.login_attempts = 0
		print("You are reseting the login apttempts")
		print(f"You have login {self.login_attempts} times")
