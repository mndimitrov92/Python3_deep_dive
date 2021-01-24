"""
Closure examples and some hints how they work.
"""

def outer(some_erg): # Free variable
	t1 = 1 # Free variable 
	t2 = 2 # Free variable

	def closure(amount=10):
		# When the method acesses variables from the outer scope it is a closure
		nonlocal t1
		print("I'm a closure.")
		t1 += amount
		print("outer parameter: {0}".format(some_erg))
		print("Arguments: {0}".format(amount))
		print("sum of t1 and t2: {0}".format(t1 + t2))
	return closure # need to return the function

# Any changes to the free cariables is applicable to this closure only
closure1 = outer(5)
closure1()
closure1()
closure1()
closure1()
print("========Closure attributes=======")
print("Free variables: ", closure1.__code__.co_freevars)
print('Closures:', closure1.__closure__)

print("========Other closure===========") 
closure2 = outer(5)
closure2(2)
closure2(3)
closure2(1)
closure2(1)