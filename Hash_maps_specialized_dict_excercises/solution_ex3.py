import json
from collections import ChainMap
from pprint import pprint


def chain_content(d1, d2):
	"""
	Recursively chain the dictionaries.
	"""
	chained = ChainMap(d1, d2)
	for key, val in d1.items():
		if isinstance(val, dict) and key in d2:
			chained[key] = chain_content(d1[key], d2[key])
	return chained


def prepare_environment(environment_name):
	"""
	Combines the settings from the environment name that has been passed and overrides the common
	properties with the custom for the specific environment ones.
	"""
	with open('common.json') as common_settings, \
		 open('%s.json' %environment_name) as custom_env:
		 common = json.load(common_settings)
		 custom = json.load(custom_env)
	merged = chain_content(custom, common)
	return dict(merged)


if __name__ == '__main__':
	pprint(prepare_environment('dev'))
