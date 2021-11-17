"""
sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]

make_filter(name='polly', type='bird').apply(sample_data)
should return only second entry from the list

There are multiple bugs in this code.
Find them all and write tests for faulty cases.
"""
from typing import Any, Callable, Dict, Hashable, Iterable, List


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria

    example of usage:
    positive_even = Filter(lambda a: a % 2 == 0,
                        lambda a: a > 0,
                        lambda a: isinstance(int, a)))
    positive_even.apply(range(100))
    should return only even numbers from 0 to 99
    """
    def __init__(self, functions: List[Callable]) -> None:
        self.functions = functions
        print(len(functions))

    def apply(self, data: Iterable) -> List[Any]:
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]


def make_filter(**keywords: Any) -> Filter:
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []

    for key, value in keywords.items():

        def wrapper(key: Hashable, value: Any) -> Callable:
            def keyword_filter_func(input_dict: Dict) -> bool:
                """
                Function return True if key value pair from enclosed scope
                while function was defined are presented in input_dict
                """
                if key in input_dict:
                    return input_dict[key] == value
                else:
                    return False
            return keyword_filter_func

        filter_funcs.append(wrapper(key, value))

    return Filter(filter_funcs)
