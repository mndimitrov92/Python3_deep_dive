"""
Decorator example implemented with a class.
"""

class MyDecorator:
	"""
	Decorator implemented with a class
	"""
	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		print(f"Decorating {self.func.__name__}")
		result = self.func(*args, **kwargs)
		print("Decoratio complete.")
		return result


@MyDecorator
def test_func(a, b):
	print("Called with:" ,a, b)
	return a+b

test_func(3, 4)
