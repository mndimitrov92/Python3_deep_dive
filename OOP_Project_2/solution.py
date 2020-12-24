from functools import total_ordering
import operator

@total_ordering
class Mod:
	"""
	Class creating creating objects for modular aritmethic.
	"""

	def __init__(self, value, modulus):
		if not isinstance(value, int):
			raise TypeError("Unsupported type for value.")
		if not isinstance(modulus, int):
			raise TypeError("Unsupported type for modulus.")
		if modulus <= 0:
			raise ValueError("Modulus must be a positive number.")
		self._modulus = modulus
		self._value = value % self._modulus

	def __eq__(self, other):
		other_val = self._get_value(other)
		return self.value == other_val

	def __lt__(self, other):
		other_val = self._get_value(other)
		return self.value < other_val

	def __add__(self, other):
		return self._perform_operation(other, operator.add)

	def __sub__(self, other):
		return self._perform_operation(other, operator.sub)

	def __mul__(self, other):
		return self._perform_operation(other, operator.mul)

	def __pow__(self, other):
		return self._perform_operation(other, operator.pow)

	def __iadd__(self, other):
		return self._perform_operation(other, operator.add, in_place=True)

	def __isub__(self, other):
		return self._perform_operation(other, operator.sub, in_place=True)

	def __imul__(self, other):
		return self._perform_operation(other, operator.mul, in_place=True)

	def __ipow__(self, other):
		return self._perform_operation(other, operator.pow, in_place=True)

	def __hash__(self):
		return hash((self.value, self.modulus))

	def __repr__(self):
		return f"Mod(value={self.value}, modulus={self.modulus})"

	def __int__(self):
		return self.value

	def _get_value(self, other):
		if isinstance(other, int):
			return other % self.modulus
		elif isinstance(other, Mod) and self.modulus ==other.modulus:
			return other.value
		raise TypeError("Incompatible types.")

	def _perform_operation(self, other, operation, in_place=False):
		other_val = self._get_value(other)
		new_value = operation(self.value, other_val)
		if in_place:
			self._value = new_value % self.modulus
			return self
		else:
			return Mod(new_value, self.modulus)

	@property
	def value(self):
		return self._value
	
	@property
	def modulus(self):
		return self._modulus
