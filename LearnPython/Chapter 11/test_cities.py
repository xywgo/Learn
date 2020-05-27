# 11-1, 11-2
import unittest
from city_function import city_country_name

class CityFunctionTest(unittest.TestCase):
	"""Test for city_function.py"""

	def test_city_function(self):
		"""does 'Santiago, Chile' work?"""
		formatted = city_country_name('santiago', 'chile')
		self.assertEqual(formatted, 'Santiago, Chile')

	def test_city_poulation_functin(self):
		"""does 'Santiago, Chile - populatin 5000000' work?"""
		formatted = city_country_name('santiago', 'chile', 5000000)
		self.assertEqual(formatted, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
	unittest.main()
