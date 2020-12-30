"""
Test casses covering part of the functionality provided in the solutions module.
These are not all the necessary tests but are enough for practise.
"""
import unittest
from solution import Resource, CPU, Storage, HDD, SSD


class TestResource(unittest.TestCase):
	"""
	Testing the functionality of the resource base class
	"""
	def setUp(self):
		self.res = Resource("test", "AMD", 100, 10)

	def tearDown(self):
		del self.res

	def test_creation_valid(self):
		self.assertIsInstance(self.res, Resource)
		self.assertEqual(self.res.name, "test")
		self.assertEqual(self.res.manufacturer, "AMD")
		self.assertEqual(self.res.total, 100)
		self.assertEqual(self.res.allocated, 10)

	def test_creation_invalid(self):
		# Test scenarios for invalid inouts for total and allocated resources
		scenarios = (
				(10, 11), # Total less than allocated
				(None, 10), # Invalid total value
				(10, None), #Invalid allocate value
				('10', '11'), # String values
				(10.0, 11.2), # Float values
				(-10, 11), # Negative total value
				(10, -11) # Negative allocated value
			)
		for scen in scenarios:
			with self.subTest(f"Test Case #{scen}"):
				with self.assertRaises(ValueError):
					Resource("Test", "AMD", *scen)

	def test_available(self):
		self.assertEqual(self.res.available, 90)

	def test_str(self):
		self.assertEqual(str(self.res), "test")

	def test_repr(self):
		self.assertEqual(repr(self.res), 
						 'resource: name=test manufacturer=AMD total=100 allocated=10')

	def test_category(self):
		self.assertEqual(self.res.category, 'resource')

	def test_claim(self):
		self.res.claim(25)
		self.assertEqual(self.res.allocated, 35)

	def test_freeup(self):
		self.res.freeup(5)
		self.assertEqual(self.res.allocated, 5)

	def test_died(self):
		self.res.died(2)
		self.assertEqual(self.res.allocated, 8)
		self.assertEqual(self.res.total, 98)

	def test_purchased(self):
		self.res.purchased(18)
		self.assertEqual(self.res.total, 118)

	def test_claim_invalid(self):
		scenarios = (
				None,
				12.3,
				"11",
				300
			)

		for scen in scenarios:
			with self.subTest(f"Test Case with value={scen}"):
				with self.assertRaises(ValueError):
					self.res.claim(scen)

	def test_freeup_invalid(self):
		scenarios = (
				None,
				12.3,
				"11",
				300
			)
		
		for scen in scenarios:
			with self.subTest(f"Test Case with value={scen}"):
				with self.assertRaises(ValueError):
					self.res.freeup(scen)

	def test_died_invalid(self):
		scenarios = (
				None,
				12.3,
				"11",
				300
			)
		
		for scen in scenarios:
			with self.subTest(f"Test Case with value={scen}"):
				with self.assertRaises(ValueError):
					self.res.died(scen)

	def test_purchased_invalid(self):
		scenarios = (
				None,
				12.3,
				"11"
			)
		
		for scen in scenarios:
			with self.subTest(f"Test Case with value={scen}"):
				with self.assertRaises(ValueError):
					self.res.purchased(scen)


class TestCPU(unittest.TestCase):
	"""
	Test cases covering the CPU specific functionality.
	"""
	def setUp(self):
		self.cpu = CPU("test", "AMD", 50, 10, 8, "AM4", 100)

	def tearDown(self):
		del self.cpu

	def test_creation(self):
		self.assertIsInstance(self.cpu, CPU)
		self.assertEqual(self.cpu.name, "test")
		self.assertEqual(self.cpu.manufacturer, "AMD")
		self.assertEqual(self.cpu.total, 50)
		self.assertEqual(self.cpu.allocated, 10)
		self.assertEqual(self.cpu.cores, 8)
		self.assertEqual(self.cpu.socket, "AM4")
		self.assertEqual(self.cpu.power_watts, 100)

	def test_creation_invalid(self):
		scen = (
			("8", "1000"), # core and watts values are strings
			(8.1, 9000.5),  # cores and watts are floats
			(None, None),
			(-4, -1000)   # cores and watts negative numbers
		)
		for item in scen:
			core, watts = item
			with self.subTest(f"Test Case with cores={core}, watts={watts}"):
				with self.assertRaises(ValueError):
					CPU("test","AMD", 100, 10, core, "AM4", watts)

	def test_category(self):
		self.assertEqual(self.cpu.category, "cpu")


class TestStorage(unittest.TestCase):
	"""
	Test cases covering the Storage specifiv functionality.
	"""
	def setUp(self):
		self.storage = Storage("test", "manufacturer", 100, 10, 250)

	def tearDown(self):
		del self.storage

	def test_creation(self):
		self.assertIsInstance(self.storage, Storage)
		self.assertEqual(self.storage.name, "test")
		self.assertEqual(self.storage.manufacturer, "manufacturer")
		self.assertEqual(self.storage.total, 100)
		self.assertEqual(self.storage.allocated, 10)
		self.assertEqual(self.storage.capacity_GB, 250)

	def test_cration_invalid(self):
		scenarios = (-250, None, 240.2, "250")
		for scen in scenarios:
			with self.subTest(f"Test Case with capacity_GB={scen}"):
				with self.assertRaises(ValueError):
					Storage("test", "manu", 100, 10, scen)

	def test_category(self):
		self.assertEqual(self.storage.category, "storage")


class TestHDD(unittest.TestCase):
	"""
	Test cases covering the HDD specific funtionality
	"""
	def setUp(self):
		self.hdd = HDD("Name", "manu", 100, 10, 250, 2.5, 7200)

	def tearDown(self):
		del self.hdd

	def test_creation(self):
		self.assertIsInstance(self.hdd, HDD)
		self.assertEqual(self.hdd.name, "Name")
		self.assertEqual(self.hdd.manufacturer, "manu")
		self.assertEqual(self.hdd.total, 100)
		self.assertEqual(self.hdd.allocated, 10)
		self.assertEqual(self.hdd.capacity_GB, 250)
		self.assertEqual(self.hdd.size, 2.5)
		self.assertEqual(self.hdd.rpm, 7200)

	def test_creation_invalid(self):
		scenarios = (7000.25, -5000, "7000", None)
		for scen in scenarios:
			with self.subTest(f"Test with rpm={scen}"):
				with self.assertRaises(ValueError):
					HDD("test", "manu", 100, 10, 250, 20, scen)

	def test_category(self):
		self.assertEqual(self.hdd.category, "hdd")


class TestSSD(unittest.TestCase):
	def setUp(self):
		self.ssd = SSD("Name", "manu", 100, 10, 250, "NVMe")

	def tearDown(self):
		del self.ssd

	def test_creation(self):
		self.assertIsInstance(self.ssd, SSD)
		self.assertEqual(self.ssd.name, "Name")
		self.assertEqual(self.ssd.manufacturer, "manu")
		self.assertEqual(self.ssd.total, 100)
		self.assertEqual(self.ssd.allocated, 10)
		self.assertEqual(self.ssd.capacity_GB, 250)
		self.assertEqual(self.ssd.interface, "NVMe")

	def test_category(self):
		self.assertEqual(self.ssd.category, "ssd")



if __name__ == '__main__':
	unittest.main()