"""
Decorators that can decorate classes and add decorators to all the needed methods.
"""
from functools import wraps
from types import FunctionType


def func_dec(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		print(f"Decorating {fn.__name__}")
		result = fn(*args, **kwargs)
		print(f"Decoration of {fn.__name__} complete.")
		return result
	return wrapper


def decorate_me(cls):
	"""
	Class decorator the decoarates only instance methods.
	"""
	for label, func in vars(cls).items():
		if isinstance(func, FunctionType):
			setattr(cls, label, func_dec(func))
	return cls


@decorate_me
class TestClass:
	class_var = (1, 2, 3)

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def method1(self):
		return "Hello"

	def method2(self):
		return "Hellow again"

	def method3(self):
		return self.x + self.y

	@classmethod
	def method4(cls):
		return	cls.class_var

	@staticmethod
	def method5():
		return "I'm static"

# The current implementation decorates onlu instance methods
t = TestClass(5, 6)
print(t.method1())
print(t.method2())
print(t.method3())
print(TestClass.method4())
print(TestClass.method5())
