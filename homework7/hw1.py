"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "RED": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


basic_types_to_compare = (int, bool, str)
all_types = (str, list, tuple, dict, set, int, bool)


class NotDictError(Exception):
    """Input tree must be dict"""


def compare_element(value: Any, element: Any) -> int:
    """Compare value and element"""
    if isinstance(element, all_types):
        return int(value == element)

    raise ValueError(f'Unsupported data type {type(value)}')


def process_branch(branch: Any, element: Any) -> int:
    """Step recursively through the branch"""
    # Check if branch is int, str or bool to stop recursion
    if isinstance(branch, basic_types_to_compare):
        result = compare_element(branch, element)
        return result

    result = 0
    for value in branch:
        result += process_value(value, element)

    return result


def process_value(value: Any, element: Any) -> int:
    """
    Check if value can be compared with element,
    else go deeper in value structure
    """
    result = 0
    # Stop recursion if value equal to element
    if isinstance(value, type(element)):
        result = compare_element(value, element)
        if result:
            return result

    # If dict -> iterate by its values
    if isinstance(value, dict):
        keys = value.keys()
        value = value.values()
        result += process_branch(keys, element)

    result += process_branch(value, element)

    return result


def find_occurrences(tree: dict, element: Any) -> int:
    """Count the number of element occurrences in tree"""

    if not isinstance(tree, dict):
        raise NotDictError

    result = 0
    for value in tree.values():
        result += process_value(value, element)
    return result


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
