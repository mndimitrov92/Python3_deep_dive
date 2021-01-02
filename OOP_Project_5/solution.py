"""
"""
from enum import Enum, unique

# The unique deorator provides a neat additional validation to disallow duplicate enum members
@unique
class AppException(Enum):
	"""
	AppException enumeration class providing an easy way to generate consistent
	exceptions containing:
	exception code, exception type, exception message
	"""
	ERROR   = (100, ValueError, "ValueError message")
	WARNING = (200, AttributeError, "AttributeError message.")

	# overriding the __new__ method allows to handle custom attributes
	# and retrieving the member by value: AppException(100)
	def __new__(cls, member_code, member_type, member_message):
		member = object.__new__(cls)
		member._value_ = member_code
		member.exc_type = member_type
		member.exc_msg = member_message
		return member # Must return the member instance

	@property
	def code(self):
		return self.value

	def throw(self, custom_msg=None):
		"""
		Throw custom error messages when passed
		"""
		msg = custom_msg or self.exc_msg
		raise self.exc_type(f"{self.code} : {msg}")
