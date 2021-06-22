from collections import Counter, defaultdict
from random import seed, choices
seed(0)


eye_colors = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")


class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color


persons = [Person(color) for color in choices(eye_colors[2:], k=50)]


def eye_color_counter(persons_list):
	"""
	Returns a dictionary with the counts of each ee color that was present in the
	passed list of person objects.
	"""
	all_eye_colors = defaultdict(int)
	counter = Counter([person.eye_color for person in persons])
	for color in eye_colors:
		all_eye_colors[color] += counter[color]
	return dict(sorted(all_eye_colors.items(), key=lambda x: x[1], reverse=True))
	

def eye_color_counter_v2(persons_list):
	"""
	Returns a dictionary with the counts of each ee color that was present in the
	passed list of person objects second approach.
	"""
	all_eye_colors = Counter({color: 0 for color in eye_colors})
	all_eye_colors.update(person.eye_color for person in persons)
	return dict(all_eye_colors.most_common())


if __name__ == '__main__':
	print(eye_color_counter(persons))
	print(eye_color_counter_v2(persons))
