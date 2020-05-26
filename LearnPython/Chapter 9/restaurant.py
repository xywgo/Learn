class Restaurant:
	"""A simple attempt for model a Restaurant"""
	def __init__(self, restaurant_name, restaurant_type):
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		# 9-4
		self.number_served = 0

	def describe_restaurant(self):
		"""print the name and type of the restaurant"""
		print(f"The resaurant name is {self.restaurant_name}.")
		print(f"The resaurant type is {self.restaurant_type}.")

	def open_restaurant(self):
		"""Tell people the restaurant is open"""
		print(f"The {self.restaurant_name} is open now.")

	# 9-4.
	def set_number_served(self, numbers):
		"""Set the served costomers number"""
		self.number_served = numbers

	def increment_number_served(self, numbers):
		"""Set the increment comstomers"""
		self.number_served += numbers