"""
Decorators which can contain additional attributes that can be accessed.
"""
from functools import wraps


def my_decorator(fn):
	my_var = {}

	@wraps(fn)
	def wrapper(*args, **kwargs):
		print("Decorating...")
		result = fn(*args, **kwargs)
		print("Finished")
		return result

	def my_helper_func():
		print("Help called")
		return my_var

	# Inner decorator that can be accessed for storing function instances
	def another_dec(some_key):
		def inner(fn):
			print("Inner decorator called")
			my_var[some_key] = fn
			return fn
		return inner
	# In order to access the function, it needs to be attached to the returned wrapper function
	wrapper.saved = my_helper_func()
	wrapper.add_me = another_dec 
	return wrapper


# Initial decoration of the function
@my_decorator
def test_func():
	print("Hello")
	return 5

print(test_func.saved)


# Then the the inner decorator from the decoarated function can be used to decorate other functions.
@test_func.add_me("my_func2")
def test_func2():
	print("Hello again")
	return 10
test_func2()
print(test_func.saved)