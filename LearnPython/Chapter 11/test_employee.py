import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for employee"""

    def setUp(self):
        self.my_employee = Employee('Jason', 'Chen', 20000)
        self.amounts = [5000, 6000, 7000]

    def test_give_default_raise(self):
        """Test default raise"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 20000+self.amounts[0])

    def test_give_custom_raise(self):
        """Test custom amounts"""
        self.my_employee.give_raise(self.amounts[1])
        self.assertEqual(self.my_employee.annual_salary, 20000+self.amounts[1])


if __name__ == '__main__':
    unittest.main()
