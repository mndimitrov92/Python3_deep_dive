"""
Example of stacking multiple decorators to visualize how they execute
"""
from functools import wraps

def dec_1(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		print("Dec 1 start")
		result = fn(*args, **kwargs)
		print("Dec 1 finish")
		return result
	return wrapper


def dec_2(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		print("Dec 2 start")
		result = fn(*args, **kwargs)
		print("Dec 2 finish")
		return result
	return wrapper


def dec_3(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		print("Dec 3 start")
		result = fn(*args, **kwargs)
		print("Dec 3 finish")
		return result
	return wrapper


# Stacked decorators are run from top to bottom
@dec_1
@dec_2
@dec_3
def some_func(*args, **kwargs):
	print("Executing with: ", args, kwargs)

some_func()

# The above syntax is equivalent to:
print("=====Second call========")
def some_func2(*args, **kwargs):
	print("Executing with: ", args, kwargs)

some_func = dec_1(dec_2(dec_3(some_func2)))
some_func("test")


