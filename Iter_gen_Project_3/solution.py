from collections import namedtuple, defaultdict
from datetime import datetime



class DataParser():
	"""
	Class parsing the data fields of a csv file and converting the rows into namedtuples
	"""
	MY_FILE = 'nyc_parking_tickets_extract.csv'

	def __init__(self):
		self._mydata = self._read_data()
		self.ticket = next(self._mydata)
		self._failed = []

	def _parse_data(self, data):
		"""
		Parse the data fields of the collected data and convert them
		to their appropraite format.
		"""
		date_format = '%m/%d/%Y'
		data = data.strip()
		try:
			result = int(data)
		except ValueError:
			try:
				result = datetime.strptime(data, date_format).date()
			except ValueError:
				result = str(data)
		return result

	def _parse_row(self, row):
		"""
		Function for parsing the entire row of data attributes.
		"""
		return [self._parse_data(item) for item in row.strip('\n').split(',')]

	def _read_data(self):
		"""
		Generator for parsing a file and convering the data into namedtuples
		"""
		with open(DataParser.MY_FILE) as f:
			headers = next(f).strip('\n').split(',')
			headers = [header.replace(' ', '_').lower() for header in headers]
			# Create the namedtuple
			yield namedtuple('Ticket', headers)
			for data in f:
				data = self._parse_row(data)
				# Handle only valid data where all fields are filled
				if all(data):
					try:
						yield self.ticket(*data)
					except TypeError:
						self._failed.append(data)

	@property
	def ticket_fields(self):
		return self.ticket._fields

	def show_data(self, amount=1):
		"""
		Iterator method which shows amount rows of the data.
		"""
		for _ in range(amount):
			print(next(self._mydata))

	def num_violation_per_carmake(self):
		"""
		Retireves the number of violations per car make. 
		"""
		car_makes = defaultdict(int)
		for item in self._mydata:
			car_makes[item.vehicle_make] += 1
		return car_makes


if __name__ == '__main__':
	data = DataParser()
	print(data.ticket_fields)
	print(data.num_violation_per_carmake())
	

