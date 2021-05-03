"""
Example script of a cooperative coroutine implementation using generators and deque. 
"""
from collections import deque


def producer(dq, amount):
	"""
	Generator function
	Produce and populate the deque until it reaches it's max amount and then suspend.
	"""
	print("Populating deque...")
	for x in range(amount):
		dq.append(x)
		if len(dq) == dq.maxlen:
			print("Queue full! Suspending action.")
			yield  # only used to suspend the generator until the consumer collects the items


def consumer(dq):
	"""
	Generator function that consumes all the elements in the queue.
	""" 
	while True:
		while len(dq):
			print("Processing element", dq.pop())
		print("All elements processed! Suspending action")
		yield # Again only needed to suspend the generator so the consumet can take over again


def coordinator():
	"""
	Function to coordinate the consumer and producer
	"""
	# create the deque and add the max allowed amount
	dq = deque(maxlen=5)
	# create the generator objects of the consumer and producer
	prod = producer(dq, 40)
	con = consumer(dq)
	while True:
		try:
			# Start producing the elements 
			print("Producing...")
			next(prod)
		except StopIteration:
			# break our of the loop once the deque has been exhausted
			break
		finally:
			# Consume all the elements that were placed in the queue
			print("Consuming...")
			next(con)


# ====================================================================
# The yield expression could also be used to receive data
def yield_as_data_receiver():
	"""
	In the generator the yield statement could also be assigned to a variable
	and then returned from the generator. First needs to be primed (i.e in a Suspended state)
	And then using the send method you can pass the additional value
	"""
	while True:
		received = yield
		print(f"You said: {received}")

# ====================================================================
# Simple example of a two way communication between generators
def subgen():
	yield "Line 1"
	yield "Line 1"

def my_gen():
	g = subgen()
	# Once we reach this place the yielding is being delegated to the subgen
	# which in turn passes the output to this generagor until it raises StopIteration.
	# Afterwards thisgenerator yields it's value
	yield from g
	yield "Finished"


if __name__ == '__main__':
	coordinator()
	#### the below illustrates how the generator can received additional values
	print("==="*30)
	# Create the generator
	gen = yield_as_data_receiver()
	# Prime it
	next(gen)
	# Send the data
	gen.send("Hello there")
	print("==="*30)
	gen = my_gen()
	print(next(gen))
	print(next(gen))
	print(next(gen))