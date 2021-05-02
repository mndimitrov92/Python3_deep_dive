from collections import namedtuple
from contextlib import contextmanager
import csv

MY_FILES = 'cars.csv', 'personal_info.csv'


## Solution for Goal 1 of he project
class CsvReader:
	"""
	Context manager for opening csv files and returning namedtuples
	for each of the rows implemented as an iterator
	"""
	def __init__(self, filename):
		self.filename = filename
		self.data = None

	def __enter__(self):
		with open(self.filename) as f:
			sample = f.read(2000)
			dialect = csv.Sniffer().sniff(sample)
		self._f = open(self.filename)
		self.reader = csv.reader(self._f, dialect)
		self.data = namedtuple('Data', next(self.reader))
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		self._f.close()
		return False

	def __iter__(self):
		return self

	def __next__(self):
		return self.data(*next(self.reader))


for each_file in MY_FILES:
	with CsvReader(each_file) as r:
		print(next(r))
		print(next(r))
		print(next(r))


print("=" * 60)
## Solution of Goal 2 of the project


@contextmanager
def file_reader(f_name):
	def parse_data_reader(iterator, named_tuple):
		"""
		Generator function that yields named_tuples of the rows of the iterator
		"""
		for row in iterator:
			yield named_tuple(*row)
	
	with open(f_name) as f:
		sample = f.read(2000)
		dialect = csv.Sniffer().sniff(sample)
	my_file = open(f_name)
	try:
		reader = csv.reader(my_file, dialect)
		data = namedtuple('Data', next(reader))
		yield parse_data_reader(reader, data)
	finally:
		my_file.close()


for each_file in MY_FILES:
	with file_reader(each_file) as r:
		print(next(r))
		print(next(r))
		print(next(r))