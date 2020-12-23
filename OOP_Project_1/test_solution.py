import unittest
from datetime import datetime
from solution import Account


class TestAccount(unittest.TestCase):
	"""
	Test cases verifying the correct behavior of the Account
	"""

	def setUp(self):
		self.acc1 = Account(1234, "John", "Smith")

	def tearDow(self):
		del self.acc1

	def _get_time(self):
		curr_time = datetime.utcnow()
		return datetime.strftime(curr_time, "%Y%m%d_%H%M%S")

	def test_account_init(self):
		"""
		Test initialization with correct values.
		"""
		self.assertIsInstance(self.acc1, Account)

	def test_account_properties(self):
		"""
		Test initial account properties
		"""
		self.assertEqual(self.acc1.first_name, "John")
		self.assertEqual(self.acc1.last_name, "Smith")
		self.assertEqual(self.acc1.full_name, "John Smith")
		self.assertEqual(self.acc1.balance, 0)
		self.assertEqual(Account.get_interest_rate(), 0.05)
		self.assertEqual(str(Account.TRANSACTION_ID), 'count(1000)')

	def test_invalid_first_name(self):
		"""
		Test invalid first name setting raises an error.
		"""
		invalids = ("", 123, None)
		for i, item in enumerate(invalids):
			# Testing sub test cases
			with self.subTest(test_name=f"Test #{i}"):
				self.assertRaises(ValueError, setattr, self.acc1, 'first_name', item)
		self.assertEqual(self.acc1.first_name, "John")

	def test_invalid_last_name(self):
		"""
		Test invalid last name setting raises an error.
		"""
		with self.assertRaises(ValueError):
			self.acc1.last_name = ""
			self.acc1.last_name = None
			self.acc1.last_name = 123
		self.assertEqual(self.acc1.last_name, "Smith")

	def test_name_change(self):
		"""
		Test that names can be changed.
		"""
		self.acc1.first_name = "Mark"
		self.acc1.last_name = "Johnson"
		self.assertEqual(self.acc1.first_name, "Mark")
		self.assertEqual(self.acc1.last_name, "Johnson")
		self.assertEqual(self.acc1.full_name, "Mark Johnson")


	def test_balance(self):
		"""
		Test initial balance value.
		"""
		self.assertEqual(self.acc1.balance, 0)

	def test_balance_change(self):
		"""
		Test that balance is updated correctly.
		"""
		self.acc1.balance = 1000
		self.assertEqual(self.acc1.balance, 1000)

	def test_invalid_balance(self):
		"""
		Test that negative balance should not be possible.
		"""
		with self.assertRaises(ValueError):
			self.acc1.balance = -2000

	def test_deposit(self):
		"""
		Test thet by depositing the amount is being updated.
		"""
		code = self.acc1.deposit(500)
		self.assertEqual(self.acc1.balance, 500)
		# @TODO: mock code generation so the tests fors not depend on execution order
		self.assertEqual(code, "D-1234-{}-1000".format(self._get_time()))

	def test_withdraw(self):
		"""
		Test withdrawing from the account is possible
		"""
		self.acc1.balance = 1200
		code = self.acc1.withdraw(800)
		self.assertEqual(self.acc1.balance, 400)
		self.assertEqual(code, "W-1234-{}-1005".format(self._get_time()))

	def test_invalid_withdraw(self):
		"""
		Withdrawing amount >  account balance should not be possible.
		"""
		self.acc1.balance = 1200
		code = self.acc1.withdraw(1500)
		self.assertEqual(self.acc1.balance, 1200)
		self.assertEqual(code, "X-1234-{}-1003".format(self._get_time()))

	def test_pay_interest(self):
		"""
		Test that the interest rate is being added to the account.
		"""
		new_acc = Account(3333, "S", "S", 1000)
		code = new_acc.pay_interest()
		self.assertEqual(new_acc.balance, 1050)
		self.assertEqual(code, "I-3333-{}-1004".format(self._get_time()))

	def test_interest_rate_change(self):
		"""
		Test that the interest rate can be changed.
		"""
		Account.set_interest_rate(0.2)
		self.acc1.deposit(1000)
		self.acc1.pay_interest()
		self.assertEqual(Account.get_interest_rate(), 0.2)
		# Revert back to initial value
		Account.set_interest_rate(0.05)
		self.assertEqual(self.acc1.balance, 1200)

	def test_invalid_interest_rate(self):
		"""
		Test that setting an invalid interest rate should not be possible
		"""
		with self.assertRaises(ValueError):
			Account.set_interest_rate(-50)
			Account.set_interest_rate(1+2j)
			Account.set_interest_rate("123")
		self.assertEqual(Account.get_interest_rate(), 0.05)

	def test_parse_confirmation_code(self):
		"""
		Confirmation code could be split into chunks.
		"""
		example_code = "W-1111-20201222_184506-1005"
		result = Account.parse_confirmation_code(example_code)
		self.assertEqual(result.account_number, "1111")
		self.assertEqual(result.transaction_type, "W")
		self.assertEqual(result.date_utc, "2020-12-22T18:45:06")
		self.assertEqual(result.transaction_id, "1005")

	def test_parse_invalid_confirmation_code(self):
		"""
		Parsing a confirmartion code with invalid date should raise an error.
		"""
		invalid_code = "W-1111-20201332_999999-1005"
		self.assertRaises(ValueError, Account.parse_confirmation_code, invalid_code)


if __name__ == '__main__':
	unittest.main()
