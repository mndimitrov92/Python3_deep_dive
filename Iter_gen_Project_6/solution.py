import csv
from contextlib import contextmanager


def parse_data(filename):
	"""
	Csv file parser.
	"""
	with open(filename) as f:
		dialect = csv.Sniffer().sniff(f.read(2000))
		f.seek(0) # Return the currsor back to the beginning
		next(f) # Skip header
		yield from csv.reader(f, dialect)


def coroutine(fn):
	"""
	Decorator for priming coroutines.
	"""
	def inner(*args, **kwargs):
		corr =fn(*args, **kwargs)
		next(corr) # Priming the coroutine
		return corr 
	return inner


@coroutine
def save_to_file(f_name):
	with open(f_name, 'w', newline='') as f:
		writer = csv.writer(f)
		while True:
			data = yield
			writer.writerow(data)

@coroutine
def filter_data(filter_pred, target):
	"""
	Filter function applying the filter predicate to the passed data and sending it to
	the target.
	"""
	while True:
		row = yield 
		if filter_pred(row):
			target.send(row)


@coroutine
def pipeline_coroutine(out_file, name_filters):
	save = save_to_file(out_file)
	filtered = save
	for filter_name in name_filters:
		filtered = filter_data(lambda row, v=filter_name: v in row[0], filtered)

	while True:
		received = yield
		filtered.send(received)


@contextmanager
def pipeline(out_file, name_filters):
	p = pipeline_coroutine(out_file, name_filters)
	try:
		yield p 
	finally:
		p.close()


with pipeline('output.csv', ('Chevrolet', 'Carlo')) as p:
	for row in parse_data('cars.csv'):
		p.send(row)


