d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}


def combine_data(*args):
	"""
	Combines the data from multiple dictionaries and returns a single one with all the data
	and the frequency of each item, sorted in a descending order.
	"""
	my_dict = {}
	for d in args:
		for k,v in d.items():
			try:
				my_dict[k]
			except KeyError:
				my_dict[k] = v
			else:
				my_dict[k] += v
	return dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))


if __name__ == '__main__':
	print(combine_data(d1, d2, d3))
	print(combine_data(d1, d2))
