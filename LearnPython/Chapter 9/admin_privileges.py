
from user import User

class Privileges:
	"""A separate privileges class"""
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		"""show the Admin privileges"""
		print("privileges")
		for privilege in self.privileges:
			print(f"\t - {privilege}")


class Admin(User):
	"""An administrator user modle"""
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()