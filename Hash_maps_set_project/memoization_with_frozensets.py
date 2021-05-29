"""
Memoizing decorators using frozensets. Handy for handling cases
where the order of the key word arguments is being changed or when the
order of arguments is irrelevant or when the args/kwargs are not hashable.
"""
def memoizer(fn):
	"""
	Handles cases also when the order of the kwargs is switched.
	"""
	cache = {}
	def inner(*args, **kwargs):
		key = (*args, frozenset(kwargs.items()))
		if key not in cache:
			cache[key] = fn(*args, **kwargs)
		return cache[key]
	return inner

@memoizer
def test1(*, a, b):
	print(f"calculating {a+b}")
	return a+b


#the function is only called once
print(test1(a=10, b=2))
print(test1(a=10, b=2))
print(test1(b=2, a=10))


def memoizer_2(fn):
	"""
	Handles cases also when the order of the kwargs is switched and when the order of args
	is irrelevant
	"""
	cache = {}
	def inner(*args, **kwargs):
		# get the union of all args and kwargs and use it for the cache
		key = frozenset(args) | frozenset(kwargs.items())
		if key not in cache:
			cache[key] = fn(*args, **kwargs)
		return cache[key]
	return inner


@memoizer_2
def test2(*args):
	print(f"calculating {sum(args)}")
	return sum(args)

#the function is only called once 
print(test2(1,2,3))
print(test2(3,2,1))
print(test2(3,1,2))
