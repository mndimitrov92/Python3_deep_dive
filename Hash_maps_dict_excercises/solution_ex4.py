n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}


def main(node1, node2, node3):
	# Keys present in all nodes
	common_keys = node1.keys() & node2.keys() & node3.keys()
	# Keys present in at least on of the nodes
	all_keys = node1.keys() | node2.keys() | node3.keys()
	filtered_keys = all_keys - common_keys
	return {
		key : (node1.get(key, 0), node2.get(key, 0), node3.get(key, 0))
		for key in filtered_keys
	}



if __name__ == '__main__':
	print(main(n1, n2, n3))
