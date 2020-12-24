import unittest
from solution import Mod


class TestMod(unittest.TestCase):
	"""
	Test cases for the mod functionality.
	"""
	def setUp(self):
		self.mod = Mod(19, 12)

	def tearDown(self):
		del self.mod

	def test_object_creation(self):
		mod_2 = Mod(4, 3)
		self.assertTrue(mod_2)
		self.assertEqual(mod_2.value, 1) # Value should be converted to the residue
		self.assertEqual(mod_2.modulus, 3)

	def test_initializers(self):
		scenarios = (
			("123","3"),
			(12.4, 3.4),
			(None, None),
			(1+2j, 2+1j),
			)
		for scenario in scenarios:
			with self.subTest(f"Scenario with {scenario}."):
				with self.assertRaises(TypeError):
					Mod(*scenario)
	
	def test_modulus(self):
		with self.assertRaises(ValueError):
			Mod(19, -4)
			Mod(0, 0)

	def test_representation(self):
		expected = "Mod(value=7, modulus=12)"
		self.assertEqual(repr(self.mod), expected)

	def test_hashable(self):
		d = {}
		d[self.mod] = "test"
		self.assertIn(self.mod, d)

	def test_int_casting(self):
		self.assertEqual(int(self.mod), self.mod.value)

	def test_equality_mod(self):
		self.assertEqual(self.mod, Mod(7, 12))

	def test_equality_int(self):
		self.assertEqual(self.mod, 31)

	def test_equality_different_mod(self):
		with self.assertRaises(TypeError):
			self.mod == Mod(7,18)

	def test_equality_invalid(self):
		with self.assertRaises(TypeError):
			self.mod == "31"
			self.mod == 4+8j
			self.mod == None
			self.mod == 31.0

	def test_addition_mod(self):
		new_mod = self.mod + Mod(2, 12)
		self.assertEqual(new_mod, Mod(9, 12))

	def test_addition_int(self):
		new_mod = self.mod + 2
		self.assertEqual(new_mod, Mod(9, 12))

	def test_addition_diff_modulus(self):
		with self.assertRaises(TypeError):
			self.mod + Mod(2, 13)

	def test_addition_invalid(self):
		with self.assertRaises(TypeError):
			self.mod + "31"
			self.mod + 4+8j
			self.mod + None
			self.mod + 31.0

	def test_inplace_addition(self):
		self.mod += 2
		self.assertEqual(self.mod, Mod(9, 12))

	def test_subtraction_mod(self):
		new_mod = self.mod - Mod(2, 12)
		self.assertEqual(new_mod, Mod(5, 12))

	def test_subtraction_int(self):
		new_mod = self.mod - 2
		self.assertEqual(new_mod, Mod(5, 12))

	def test_subtraction_diff_modulus(self):
		with self.assertRaises(TypeError):
			self.mod - Mod(2, 13)

	def test_subtraction_invalid(self):
		with self.assertRaises(TypeError):
			self.mod - "31"
			self.mod - 4+8j
			self.mod - None
			self.mod - 31.0

	def test_subtraction_inplace(self):
		self.mod -= 2
		self.assertEqual(self.mod, Mod(5, 12))

	def test_multiplication_mod(self):
		new_mod = self.mod * Mod(2, 12)
		self.assertEqual(new_mod, Mod(2, 12))

	def test_multiplication_int(self):
		new_mod = self.mod * 2
		self.assertEqual(new_mod, Mod(2, 12))

	def test_multiplication_diff_modulus(self):
		with self.assertRaises(TypeError):
			self.mod * Mod(2, 13)

	def test_multiplication_invalid(self):
		with self.assertRaises(TypeError):
			self.mod * "31"
			self.mod * 4+8j
			self.mod * None
			self.mod * 31.0

	def test_multiplication_inplace(self):
		self.mod *= 2
		self.assertEqual(self.mod, Mod(2, 12))

	def test_power_mod(self):
		new_mod = self.mod ** Mod(2, 12)
		self.assertEqual(new_mod, Mod(1, 12))

	def test_power_int(self):
		new_mod = self.mod ** 2
		self.assertEqual(new_mod, Mod(1, 12))

	def test_power_diff_modulus(self):
		with self.assertRaises(TypeError):
			self.mod ** Mod(2, 13)

	def test_power_invalid(self):
		with self.assertRaises(TypeError):
			self.mod ** "31"
			self.mod ** 4+8j
			self.mod ** None
			self.mod ** 31.0

	def test_power_inplace(self):
		self.mod **= 2
		self.assertEqual(self.mod, Mod(1, 12))

	def test_comparison_lt(self):
		self.assertLess(self.mod, Mod(8, 12))
		self.assertLess(self.mod, 8)

	def test_comparison_lt_invalid(self):
		with self.assertRaises(TypeError):
			self.mod < "31"
			self.mod < 4+8j
			self.mod < None
			self.mod < 31.0

	def test_comparison_le(self):
		self.assertLessEqual(self.mod, Mod(19, 12))
		self.assertLessEqual(self.mod, 19)

	def test_comparison_le_invalid(self):
		with self.assertRaises(TypeError):
			self.mod <= "31"
			self.mod <= 4+8j
			self.mod <= None
			self.mod <= 31.0


if __name__ == '__main__':
	unittest.main()
