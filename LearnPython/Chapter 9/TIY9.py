# 9-1.Restaurant:
from restaurant import Restaurant



my_restaurant = Restaurant('新园', '中餐')
print(f"My restaurant's name is {my_restaurant.restaurant_name}.")
print(f"My restaurant's type is {my_restaurant.restaurant_type}")


# 9-2 Three Restaurant:
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('Soco', 'westfood')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()


# 9-3 Users:
from user import User
user1 = User('Jason', "Parker")
user1.describe_user()
user1.greet_user()

# 9-4. Number Served:

restaurant = Restaurant('Cocox', 'snap food')
print("\n")
restaurant.describe_restaurant()
print(f"We have served {restaurant.number_served} costomers.")
restaurant.set_number_served(3)
print(f"We have served {restaurant.number_served} costomers.")
restaurant.increment_number_served(5)
print(f"We have served {restaurant.number_served} costomers.")

# 9-5. Login Attempts:
print("\n")
user2 = User('Jacob', 'Chason')
user2.describe_user()
user2.increment_login_attempts()
user2.increment_login_attempts() 
user2.reset_login_attempts()

# 9-6. Ice Cream Stand:
class IceCreamStand(Restaurant):
	"""A simple attempts to model a ice cream stand"""

	def __init__(self, restaurant_name, restaurant_type):
		super().__init__(restaurant_name, restaurant_type)
		self.flavors = ['chocolate', 'vanilla', 'strawberry']

	def flavors_list(self):
		"""Print the list of all flavors"""
		print("\n We have these flavors:")
		for flavor in self.flavors:
			print(f"\t- {flavor.title()}")

icecreamstand = IceCreamStand('Summer Feast', 'Snaps')
icecreamstand.flavors_list()

# 9-7.Admin
# 9-8
from admin_privileges import Admin
xy = Admin('Adam', 'Shane')
xy.privileges.show_privileges()

# 9-8. Privileges:

# 9-9. Battery Upgrade
# see electric_car.py

# 9-10.Import Restaurant

# 9-11

# 9-12

# 9-13. Dice:
from random import randint
class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		"""Get a random number between certain range"""
		number = randint(1, self.sides)
		print(f"You are roll {self.sides}-sided die,You get a number:")
		print(number)

die = Die()
die1 = Die(10)
die2 = Die(20)

for i in list(range(1,11)):
	print(f"The {i}st time roll:")
	die.roll_die()
	die1.roll_die()
	die2.roll_die()
	print("\n")

# 9-14. Lottery:
import random


lottery = list(range(10))

for i in list(range(5)):
	s  = random.randint(65,90)
	r = chr(s)
	lottery.append(r)

win_prize = []
for i in list(range(4)):
	choice = random.choice(lottery)
	win_prize.append(choice)

print(win_prize)


#9-16 Python module of the Week:

