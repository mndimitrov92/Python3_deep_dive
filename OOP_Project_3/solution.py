
class Resource:
	"""
	Base class containing the common functionalities between the different resources.
	In this case (CPU, HDD, SSD).
	"""
	def __init__(self, name, manufacturer, total, allocated):
		self._name = name
		self._manufacturer = manufacturer
		self._total = self._base_validation(total)
		self._allocated = self._additional_validation(allocated, self.total)

	def __str__(self):
		return self.name

	def __repr__(self):
		return f"{self.category}: name={self.name} " \
				f"manufacturer={self.manufacturer} total={self.total}" \
				f" allocated={self.allocated}"

	def _base_validation(self, item):
		"""
		Checks if the item is a positive integer
		"""
		if not isinstance(item , int) or item <= 0:
			raise ValueError("You must provide a positive integer value.")
		return item 

	def _additional_validation(self, item, max_value=0):
		"""
		Basic checks for the allocated resources.
		"""
		valid_input = self._base_validation(item)
		if valid_input >= max_value:
			raise ValueError(f"Resources could not be more than {max_value}.")
		return valid_input

	@property
	def category(self):
		return self.__class__.__name__.lower()

	@property
	def available(self):
		return self.total - self.allocated

	@property
	def name(self):
		return self._name
	
	@property
	def manufacturer(self):
		return self._manufacturer

	@property
	def total(self):
		return self._total

	@property
	def allocated(self):
		return self._allocated

	def claim(self, n):
		"""
		Takes n amount of resources from the pool.
		"""
		num = self._additional_validation(n, self.available)
		self._allocated += num

	def freeup(self, n):
		"""
		Returns n amount resource to the pool.
		"""
		num = self._additional_validation(n, self.allocated)
		self._allocated -= num

	def died(self, n):
		"""
		Returns and permamnently remove inventory from the pool.
		"""
		num = self._additional_validation(n, self.allocated)
		num = self._additional_validation(num, self.total)
		self._total -= num
		self._allocated -= num

	def purchased(self, n):
		"""
		Adds resources to the pool.
		"""
		num = self._base_validation(n)
		self._total += num


class CPU(Resource):
	"""
	Class for the CPU resource.
	"""

	def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
		super().__init__(name, manufacturer, total, allocated)
		self._cores = self._base_validation(cores)
		self._socket = socket
		self._power_watts = self._base_validation(power_watts)

	@property
	def cores(self):
		return self._cores
	
	@property
	def socket(self):
		return self._socket

	@property
	def power_watts(self):
		return self._power_watts


class Storage(Resource):
	"""
	Intermediate class for the storage type resources.
	"""
	def __init__(self, name, manufacturer, total, allocated, capacity_GB):
		super().__init__(name, manufacturer, total, allocated)
		self._capacity_GB = self._base_validation(capacity_GB)

	@property
	def capacity_GB(self):
		return self._capacity_GB


class HDD(Storage):
	"""
	Class for the HDD resource.
	"""
	def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
		super().__init__(name, manufacturer, total, allocated, capacity_GB)
		self._size = size
		self._rpm = self._base_validation(rpm)

	@property
	def size(self):
		return self._size

	@property
	def rpm(self):
		return self._rpm


class SSD(Storage):
	"""
	Class for the SSD resource.
	"""
	def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
		super().__init__(name, manufacturer, total, allocated, capacity_GB)
		self._interface = interface

	@property
	def interface(self):
		return self._interface

