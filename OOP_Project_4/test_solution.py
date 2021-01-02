from solution import IntegerField, CharField
import unittest


class TestIntegerField(unittest.TestCase):
	"""
	Test cases for the IntegerField descriptor class.
	"""

	def setUp(self):
		self.test = TestIntegerField._create_test_class(1, 50)

	def tearDown(self):
		del self.test

	@staticmethod
	def _create_test_class(min_val, max_val):
		StubClass = type("StubClass", (), {"age": IntegerField(min_val, max_val)})
		return StubClass()

	def test_initialization(self):
		self.assertEqual(type(self.test).age._min_val, 1)
		self.assertEqual(type(self.test).age._max_val, 50)

	def test_prop_name(self):
		self.assertEqual(type(self.test).age.prop_name, 'age')

	def test_get_value_class(self):
		self.assertIsInstance(type(self.test).age, IntegerField)

	def test_get_value_instance(self):
		self.assertIsNone(self.test.age)
		self.test.age = 20
		self.assertEqual(self.test.age, 20)
		self.assertIn(type(self.test).age.prop_name, self.test.__dict__)

	def test_set_value(self):
		self.test.age = 45
		self.assertEqual(self.test.__dict__[type(self.test).age.prop_name], 45)

	def test_set_value_invalid(self):
		scenarios = ("12", -22, 100, 20.5, 1+2j, None)
		for scen in scenarios:
			with self.subTest(f"Test with value={scen}"):
				with self.assertRaises(ValueError):
					self.test.age = scen

	def test_min_value_only(self):
		min_ = 0
		max_ = None
		obj = TestIntegerField._create_test_class(min_, max_)
		values = range(min_, min_ + 50, 10)
		for i in values:
			with self.subTest(f"Tested with value={i}"):
				obj.age = i
				self.assertEqual(obj.age, i)

	def test_max_value_only(self):
		min_ = None
		max_ = 100
		obj = TestIntegerField._create_test_class(min_, max_)
		values = range(max_-50, max_ , 10)
		for i in values:
			with self.subTest(f"Tested with value={i}"):
				obj.age = i
				self.assertEqual(obj.age, i)


class TestCharField(unittest.TestCase):
	"""
	Test cases for the charfield descriptor class.
	"""
	def setUp(self):
		self.test = TestCharField._create_test_class(1, 10)

	def tearDown(self):
		del self.test

	@staticmethod
	def _create_test_class(min_val, max_val):
		StubClass = type("StubClass", (), {"name": CharField(min_val, max_val)})
		return StubClass()

	def test_initialization(self):
		self.assertEqual(type(self.test).name._min_val, 1)
		self.assertEqual(type(self.test).name._max_val, 10)

	def test_prop_name(self):
		self.assertEqual(type(self.test).name.prop_name, 'name')

	def test_get_value_class(self):
		self.assertIsInstance(type(self.test).name, CharField)

	def test_get_value_instance(self):
		self.assertIsNone(self.test.name)
		self.test.name = "John"
		self.assertEqual(self.test.name, "John")
		self.assertIn(type(self.test).name.prop_name, self.test.__dict__)

	def test_set_value(self):
		self.test.name = "John"
		self.assertEqual(self.test.__dict__[type(self.test).name.prop_name], "John")

	def test_set_value_invalid(self):
		scenarios = (-22, 100, 20.5, 1+2j, None, "Some long text for testing", "")
		for scen in scenarios:
			with self.subTest(f"Test with value={scen}"):
				with self.assertRaises(ValueError):
					self.test.name = scen

	def test_min_value_only(self):
		min_ = 0
		max_ = None
		obj = TestCharField._create_test_class(min_, max_)
		values = range(min_, min_ + 10, 2)
		for i in values:
			text = "w"*i
			with self.subTest(f"Tested with value={text}"):
				obj.name = text
				self.assertEqual(obj.name, text)

	def test_max_value_only(self):
		min_ = None
		max_ = 40
		obj = TestCharField._create_test_class(min_, max_)
		values = range(max_-20, max_ , 2)
		for i in values:
			text = "w"*i
			with self.subTest(f"Tested with value={text}"):
				obj.name = text
				self.assertEqual(obj.name, text)


if __name__ == '__main__':
	unittest.main()