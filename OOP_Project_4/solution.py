"""
Module containing two data descriptors providing 
some additional validation when assinging values to a property.
"""

class BaseValidator:
	"""
	Base class containing the common functionality between the different descriptors.
	"""
	def __init__(self, min_val=None, max_val=None):
		self._min_val = min_val
		self._max_val = max_val

	def __set_name__(self, owner_class, prop_name):
		self.prop_name = prop_name 

	def __get__(self, instance, owner_class):
		if instance is None:
			return self
		return instance.__dict__.get(self.prop_name, None)

	def validate(self, value):
		"""
		Must be implementedby the inheriting class
		"""
		return NotImplemented

	def __set__(self, instance, value):
		self.validate(value)
		instance.__dict__[self.prop_name] = value


class IntegerField(BaseValidator):
	"""
	Integer descriptor only allowing itegral values [min;max].
	"""
	def validate(self, value):
		if not isinstance(value, int):
			raise ValueError(f"{self.prop_name} must be an integer.")
		if self._min_val is not None and value < self._min_val:
			raise ValueError(f"{self.prop_name} must be higher than {self._min_val}")
		if self._max_val is not None and value > self._max_val:
			raise ValueError(f"{self.prop_name} must be lower than {self._max_val}")


class CharField(BaseValidator):
	"""
	Character descriptor only allowing strings with length [min;max]
	"""
	def __init__(self, min_val=None, max_val=None):
		min_val = min_val or 0
		min_val = max(min_val, 0)
		super().__init__(min_val, max_val)

	def validate(self, value):
		if not isinstance(value, str):
			raise ValueError(f"{self.prop_name} must be a str.")
		if self._min_val is not None and len(value) < self._min_val:
			raise ValueError(f"{self.prop_name} must be more than {self._min_val} characters")
		if self._max_val is not None and len(value) > self._max_val:
			raise ValueError(f"{self.prop_name} must be less than {self._max_val} characters")

