from collections import defaultdict, Counter


d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}


def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v
            
    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))


def merge_default_dict(*dicts):
	"""
	Merge an arbitrary number of dictionaries and sort by their frequency using defaultdict.
	"""
	merged = defaultdict(int)
	for dict_ in dicts:
		for k, v in dict_.items():
			merged[k] += v
	return dict(sorted(merged.items(), key=lambda x: x[1], reverse=True))


def merge_counter(*dicts):
	"""
	Merge an arbitrary number of dictionaries and sort by their frequency using Counter.
	"""
	counter = Counter()
	for dict_ in dicts:
		counter.update(dict_)
	return dict(counter.most_common())


if __name__ == '__main__':
	print(merge_default_dict(d1, d2, d3))
	print(merge_default_dict(d1, d2))
	print("=="*20)
	print(merge_counter(d1, d2, d3))
	print(merge_counter(d1, d2))
