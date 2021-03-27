import unittest
from solution import Polygon, Polygons
import math


class TestPolygon(unittest.TestCase):
	"""
	Test cases for the Polygon class.
	"""
	def setUp(self):
		self.poly = Polygon(4, 10)

	def tearDown(self):
		del self.poly

	def assert_floats_equal(self, a,  b):
		"""
		Helper function to compare float numbers since calculating floats
		will return an approxiation so we need to set a tolerance for the calculations
		"""
		rel_tolerance = 0.001
		abs_tolerance = 0.001
		self.assertTrue(math.isclose(a, b, rel_tol=rel_tolerance, abs_tol=abs_tolerance),
						f"Output={a} ; Expected={b}")

	def test_polygon_repr(self):
		self.assertEqual(repr(self.poly), 'Polygon(n=4, R=10)')

	def test_polygon_edges(self):
		self.assertEqual(self.poly.edges, 4)

	def test_polygon_vertices(self):
		self.assertEqual(self.poly.vertices, 4)

	def test_polygon_edge_length(self):
		#self.assertEqual(self.poly.edge_length, 14.14213562373095)
		self.assert_floats_equal(self.poly.edge_length, 14.142)

	def test_area(self):
		self.assert_floats_equal(self.poly.area, 200.0)

	def test_apothem(self):
		self.assert_floats_equal(self.poly.apothem, 7.07)

	def test_perimeter(self):
		self.assert_floats_equal(self.poly.perimeter, 56.57)

	def test_interior_angle(self):
		self.assert_floats_equal(self.poly.interior_angle, 90.0)

	def test_equality(self):
		p1 = Polygon(4, 10)
		p2 = Polygon(5, 10)
		p3 = Polygon(4, 11)
		self.assertEqual(self.poly, p1)
		self.assertNotEqual(self.poly, p2)
		self.assertNotEqual(self.poly, p3)

	def test_comparison(self):
		p1 = Polygon(3, 10)
		p2 = Polygon(5, 10)
		self.assertGreater(self.poly, p1)
		self.assertLess(self.poly, p2)

	def test_invalid_polygon(self):
		self.assertRaises(ValueError, Polygon, 2, 3)
		self.assertRaises(ValueError, Polygon, 1, 3)


class TestPolygons(unittest.TestCase):
	"""
	Test cases for the Polygons iterable type class.
	"""

	def setUp(self):
		self.polys = Polygons(5, 1)

	def tearDown(self):
		del self.polys

	def test_representation(self):
		self.assertEqual(repr(self.polys), "Polygons(max_edges=5, circumradius=1)")

	def test_length(self):
		self.assertEqual(len(self.polys),  3)

	def test_iteration(self):
		for idx, poly in enumerate(self.polys, 3):
			self.assertEqual(poly, Polygon(idx ,1))

	def test_iterable_polygons(self):
		"""
		Iterable can be iterated multiple times and is not exhausted.
		"""
		self.assertEqual(list(self.polys),
						[Polygon(3, 1), Polygon(4, 1), Polygon(5, 1)])
		self.assertEqual(list(self.polys),
						[Polygon(3, 1), Polygon(4, 1), Polygon(5, 1)])

	def test_poly_iterator(self):
		"""
		Iterator is being exhausted.
		"""
		iterator = self.polys.PolyIterator(5, 3)
		self.assertEqual(list(iterator), 
						[Polygon(3, 3), Polygon(4, 3), Polygon(5, 3)])
		self.assertEqual(list(iterator), [])

	def test_iterator_returns_self(self):
		iterator = self.polys.PolyIterator(5, 3)
		self.assertEqual(id(iterator), id(iter(iterator)))


if __name__ == '__main__':
	unittest.main()