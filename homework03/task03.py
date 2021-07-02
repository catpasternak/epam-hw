# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


# example of usage:
# positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)]) # fixed
# positive_even.apply(range(100)) should return only even numbers from 0 to 99                  # check


def make_filter(**keywords):
    """Generate filter object for specified keywords"""
    filter_funcs = []

    for key, value in keywords.items():

        def func_for_filter(key, value):
            def keyword_filter_func(data_elem):  # value changed to data_elem
                try:
                    return data_elem[key] == value  # value[key] to data_elem[key]
                except KeyError:  # added exception
                    return False

            return keyword_filter_func

        filter_funcs.append(func_for_filter(key, value))

    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

# filt_obj = make_filter(name='polly', type='bird')
# print('Here comes output for name=polly, type=bird')
# print(filt_obj.apply(sample_data))
# filt_obj2 = make_filter(name='polly', occupation='was here')
# print('Here comes output for name=polly, occupation=was here')
# print(filt_obj2.apply(sample_data))

# make_filter(name="polly", type="bird").apply(sample_data)
# should return only second entry from the list
# There are multiple bugs in this code. Find them all and write tests for faulty cases.
