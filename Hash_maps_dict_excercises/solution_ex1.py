composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

def sort_dict(dict_in):
	"""
	Function that sorts and returns a sorted version of the dictionary based on the values.
	"""
	return dict(sorted(dict_in.items(), key=lambda x: x[1]))


if __name__ == '__main__':
	print(sort_dict(composers))
