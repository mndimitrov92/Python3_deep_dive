class SimpleContextManager:
	"""
	Simple context manager structure. 
	Usage:
	with SimpleContextManager() as sm:
		...
	This is equivalent to:
	ctx = SimpleContextManager()
	with ctx as sm
	"""
	def __init__(self):
		print("Initializing")
		self.obj = "[[My Object]]"

	def __enter__(self):
		"""
		The enter method needed for the context manager protocol.
		It is being called when the with statements is invoked.
		"""
		print("Entering context manager")
		# Whatever is returned here is being passed to the symbol after the 'as' keyword
		return self.obj

	def __exit__(self, exc_type, exc_value, exc_tb):
		"""
		The exit method needed for the context manager protocol.
		It provides facilities for exception handling.
		"""
		print("Exiting context manager")
		if exc_type is ValueError:
			return False # When the exit method returns False, the exceptions are being propagated
		return True # When the exit method returns True, the exceptions are being silenced

with SimpleContextManager() as sm:
	print("Within Context Manager: Output from Enter method:", sm)
	raise AttributeError

print("="*20)
# The above is the same as:
t = SimpleContextManager()
with t as sm:
	print("Within Second Context Manager: Output from Enter method:", sm)
	#raise ValueError("test")


print("="*20)
# Re-entering context managers are ones that return self in their enter methods
# so they could be nested.
class ReEnteringCtx:
	"""
	Context manager which allows nesting. 
	"""
	def __init__(self, title, indent=3):
		self._indent = indent
		self._current_indent = 0
		print(title)

	def __enter__(self):
		self._current_indent += self._indent
		return self # This allows to use the instance methods and to also nest further

	def __exit__(self, ext_type, exc_value, exc_tb):
		self._current_indent -= self._indent
		return True

	def print_(self, txt):
		result = " " * self._current_indent + " * " + txt
		print(result)

with ReEnteringCtx("My Title") as ctx:
	ctx.print_("Item 1")
	ctx.print_("Item 2")
	with ctx as ctx2:
		ctx.print_("Sub Item 1")
		ctx.print_("Sub Item 2")
	ctx.print_("Item 3")

