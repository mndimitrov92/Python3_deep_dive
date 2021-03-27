"""
Refactor the two classed from Project 1 so that
the Polygon class is lazily computed
the Polygons class is an iterable (implements __iter__) and is lazily computed
P.S: Iterators implement __iter__ and __next__ methods where they return self in __iter__, the iterabled
return a new interator
"""
import math
from functools import total_ordering


@total_ordering
class Polygon:

	def __init__(self, n_vertices, circumradius):
		if n_vertices < 3:
			raise ValueError("A polygon must have at least 3 vertices.")
		self._n_vertices = n_vertices
		self._circumradius = circumradius

	def __repr__(self):
		return f"Polygon(n={self.vertices}, R={self._circumradius})"

	def __eq__(self, other):
		if not isinstance(other, Polygon):
			return NotImplemented
		return self.vertices == other.vertices and \
				self._circumradius == other._circumradius

	def __gt__(self, other):
		if not isinstance(other, Polygon):
			return NotImplemented
		return self.vertices > other.vertices

	@property	
	def vertices(self):
		return self._n_vertices

	@property
	def edges(self):
		return self.vertices

	@property
	def edge_length(self):
		if not hasattr(self, '_edge_length'):
			self._edge_length = 2 * self._circumradius * math.sin(math.pi / self.vertices)
		return self._edge_length

	@property
	def apothem(self):
		if not hasattr(self, '_apothem'):
			self._apothem = self._circumradius * math.cos(math.pi / self.vertices)
		return self._apothem

	@property
	def area(self):
		if not hasattr(self, '_area'):
			self._area = 0.5 * self.vertices * self.edge_length * self.apothem 
		return self._area

	@property
	def perimeter(self):
		if not hasattr(self, '_perimeter'):
			self._perimeter = self.vertices * self.edge_length
		return self._perimeter

	@property
	def interior_angle(self):
		"""
		Interior angle of the poligon in degrees
		"""
		if not hasattr(self, '_int_angle'):
			self._int_angle = (self.vertices - 2) * 180 / self.vertices
		return self._int_angle


class Polygons:
	"""
	Iterable type class for polygons starting from 3 upto the max number of edges.
	"""
	def __init__(self, max_edges, circumradius):
		if max_edges < 3:
			raise ValueError("The nuber of edges must be at least 3.")
		self._max_edges = max_edges
		self._circumradius = circumradius

	def __repr__(self):
		return f"Polygons(max_edges={self._max_edges}, circumradius={self._circumradius})"

	def __len__(self):
		return self._max_edges - 2

	def __iter__(self):
		return self.PolyIterator(self._max_edges, self._circumradius)

	class PolyIterator:
		"""
		Iterator for the Polygons class
		"""
		def __init__(self, max_edges, R):
			self._max_edges = max_edges
			self._R = R
			self._current = 3

		def __iter__(self):
			return self

		def __next__(self):
			if self._current > self._max_edges:
				raise StopIteration
			else:
				output = Polygon(self._current, self._R)
				self._current += 1
				return output


	