"""
Examples of basic decorators
"""
from functools import wraps

# Basic decorator
def basic(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		print("Decorating...")
		result = fn(*args, **kwargs)
		print("Decorating finished.")
		return result
	return wrapper

@basic
def test(arg1, arg2="hello"):
	print("Called with: ", arg1, arg2)

test("hello")

# Equivalent to this
print("=====Alternativa call=======")
def test2(arg1, arg2="hello"):
	print("Called with: ", arg1, arg2)

test2 = basic(test2)
test2("Hello")

#Decorator factory
print("======Decorator factory=====")
def factory(amount): # Here are the arguments that can be passed to the decorator
	def actual_decorator(fn): # where the function needs to be passed
		@wraps(fn)
		def wrapper(*args, **kwargs):
			print("Decorating with: ", amount)
			result = fn(*args, **kwargs)
			print("Decorating finished with: ", amount)
			return result
		return wrapper
	return actual_decorator

@factory(5)
def test():
	print("Hello")

test()
# This is equivalent to
print("======Decorator factory alternative call============")
def test2():
	print("Hello")

step1 = factory(10) # Calls the decorator factory which return the actual decorator
test2 = step1(test2) # Then the function is passed to the decorator
test2()
