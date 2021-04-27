import csv
from datetime import datetime
from collections import namedtuple
from itertools import chain, compress



PERSONAL_INFO = 'personal_info.csv'
EMPLOYMENT    = 'employment.csv'
UPDATE_STATUS = 'update_status.csv'
VEHICLES      = 'vehicles.csv'


def parse_data(data):
	"""
	Parse the data fields of the collected data and convert them
	to their appropraite format.
	"""
	date_format = '%Y-%m-%dT%H:%M:%SZ'
	data = data.strip()
	try:
		result = int(data)
	except ValueError:
		try:
			result = datetime.strptime(data, date_format)
		except ValueError:
			result = str(data)
	return result


def parse_row(row):
	"""
	Function for parsing the entire row of data attributes.
	"""
	return [parse_data(item) for item in row]


# Multiple iterables parsing the files
def read_file(filename):
	with open(filename) as f:
		reader = csv.reader(f, delimiter=',' ,quotechar='"')
		tuple_name = filename.split('.')[0]
		yield namedtuple(tuple_name, next(reader))
		for line in reader:
			yield parse_row(line)


# f1 = read_file(PERSONAL_INFO)
# Personal_info = next(f1)
# f2 = read_file(EMPLOYMENT)
# Employment = next(f2)
# f3 = read_file(UPDATE_STATUS)
# Update_status = next(f3)
# f4 = read_file(VEHICLES)
# Vehicles = next(f4)

# for _ in range(3):
# 	print(Personal_info(*next(f1)))
# 	print(Employment(*next(f2)))
# 	print(Update_status(*next(f3)))
# 	print(Vehicles(*next(f4)))

# ==========================================================
# Single iterable parsing all files
# Filters for omitting the duplicate ssn fields
personal_info_filter = (True, True, True, True, True)
employent_filter     = (True, True, True, False)
update_status_filter = (False, True, True)
vehicles_filter      = (False, True, True, True)
all_filters          = (personal_info_filter, employent_filter,
						update_status_filter, vehicles_filter)


def parse_field_collection(collections, is_header=True):
	"""
	Accepts a collection of iterables containing the subiterables and their corresponding
	thruth values corresponding if they will be shown or now.
	collections is a tuple containing 2 iterables within
	"""
	iterable, to_show = collections
	if is_header:
		items = next(iterable)._fields
	else:
		items = next(iterable)
	result = []
	for idx, item in enumerate(items):
		if to_show[idx]:
			result.append(item)
	return result


def filter_data(my_iter ,key=None):
	# import pdb ;pdb.set_trace()
	yield from filter(key, my_iter)


def read_files(filter_fields=None):
	"""
	Reads all csv files and produces a single namedtuple containg all the fields.
	Based on filter_fields a custom set of fields can be set.
	filter_fiels : a list of tuples coontaining bool values for each of the data sets.
				   Based on the thruthiness of the value the field will be shown
	"""
	my_files = [PERSONAL_INFO, EMPLOYMENT, UPDATE_STATUS, VEHICLES]
	iterables = [read_file(filename) for filename in my_files]
	headers = [parse_field_collection(x) for x in zip(iterables, filter_fields)]
	headers = list(chain(*headers))
	Person = namedtuple('Person', headers)
	yield namedtuple('Person', headers)
	while True:
		try:
			data = [parse_field_collection(x, is_header=False) for x in zip(iterables, filter_fields)]
			data = list(chain(*data))
			yield Person(*data)
		except StopIteration:
			break


my_gen = read_files(all_filters)
print(list(filter_data(my_gen, key=lambda row: row.ssn == '101-71-4702')))
