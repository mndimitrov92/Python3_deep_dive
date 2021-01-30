"""
Example of a sentinel value for a aparamter.
Possible usage: in cases when you want to see arg/kwargs was at all passed to a function and
do some actions based on that. This includes when a function has a default parameter (e.g. None).
This is a way to differentiate and the user passed (including None) or the function used the default one.
Applicable for python 3. Python 2 does not support the * parameter.
"""

def sentinel(arg1=object(), *, kwarg=object()):
	# Capture the id stored of the default value f the argument
	default_val = sentinel.__defaults__[0]
	default_kwarg = sentinel.__kwdefaults__['kwarg']
	if arg1 is not default_val:
		print("Argument was provided")
	else:
		print("No Argument provided.")

	if kwarg is not default_kwarg:
		print("Kwarg was provided")
	else:
		print("Kwarg was not provided.")
	print("="*20)


sentinel()
sentinel("Hello", kwarg='Hello')
sentinel(None, kwarg=None)
sentinel('', kwarg='')
sentinel([], kwarg=[])
sentinel(kwarg=[])
sentinel([])