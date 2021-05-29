template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

# This one should be a match
john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}

# Not a match
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}

# Not a match
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}


class SchemaError(Exception):
    pass


class SchemaKeyMismatch(SchemaError):
    pass


class SchemaTypeMismatch(SchemaError, TypeError):
    pass


def match_keys(data, valid, path):
    data_keys = set(data.keys())
    valid_keys = set(valid.keys())
    extra_keys = data_keys ^ valid_keys
    if extra_keys:
        key_msg = ("Mismatched keys:" + ",".join({path + "." + str(key) 
                                                  for key in extra_keys}))
        raise SchemaKeyMismatch(key_msg)


def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = "Incorrect type: " + path + "." + \
                      "expected ->" + template_type.__name__ + \
                      ", found: " + type(data_value).__name__ 
            raise SchemaTypeMismatch(err_msg)


def recurse_validate(data, template, path):
    match_keys(data, template, path)
    match_types(data, template, path)

    dict_type_keys = {key for key,value in template.items()
                      if isinstance(value, dict)}
    for key in dict_type_keys:
        sub_path = path + "." + str(key)
        sub_template = template[key]
        sub_data = data[key]
        recurse_validate(sub_data, sub_template, sub_path)


def validate(data, template):
    recurse_validate(data, template, "")


if __name__ == '__main__':
	print(validate(john, template))
	#print(validate(eric, template))
	print(validate(michael, template))
