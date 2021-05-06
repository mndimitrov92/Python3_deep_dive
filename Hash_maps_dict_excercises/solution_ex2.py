d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}


def get_common(dict1, dict2):
	"""
	Returns a dict containing the intersection of 2 dictionaries.
	"""
	return {key: (dict1[key], dict2[key]) for key in dict1.keys() & dict2.keys()}


if __name__ == '__main__':
	print(get_common(d1, d2))
