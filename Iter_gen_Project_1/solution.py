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
		return 2 * self._circumradius * math.sin(math.pi / self.vertices)

	@property
	def apothem(self):
		return self._circumradius * math.cos(math.pi / self.vertices)

	@property
	def area(self):
		return 0.5 * self.vertices * self.edge_length * self.apothem 

	@property
	def perimeter(self):
		return self.vertices * self.edge_length

	@property
	def interior_angle(self):
		"""
		Interior angle of the poligon in degrees
		"""
		return (self.vertices - 2) * 180 / self.vertices


class Polygons:
	"""
	Sequence type class for polygons starting from 3 upto the max number of edges.
	"""
	def __init__(self, max_edges, circumradius):
		if max_edges < 3:
			raise ValueError("The nuber of edges must be at least 3.")
		self._max_edges = max_edges
		self._circumradius = circumradius
		self._polygons = [Polygon(i, self._circumradius) for i in range(3, self._max_edges + 1)]

	def __repr__(self):
		return f"Polygons(max_edges={self._max_edges}, circumradius={self._circumradius})"

	def __len__(self):
		return self._max_edges - 2

	def __getitem__(self, item):
		return self._polygons[item]

	@property
	def polygons(self):
		return self._polygons


	