from homework3.task03 import make_filter

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


def test_with_multiple_kwargs_presented_in_any_data_example():
    """Testing filter with multiple kwargs presented in any data example"""
    test_result = make_filter(name='polly', type='bird').apply(sample_data)
    assert test_result == [sample_data[1]]


def test_with_one_kwarg_presented_in_any_data_example():
    """Testing filter with one kwarg presented in any data example"""
    assert make_filter(name='Bill').apply(sample_data) == [sample_data[0]]


def test_without_kwargs():
    """Testing filter without kwargs"""
    assert make_filter().apply(sample_data) == sample_data


def test_with_kwarg_presented_only_in_one_data_example():
    """Testing filter with kwarg presented only in one data example"""
    assert not make_filter(kind='000').apply(sample_data)


def test_with_kwarg_not_in_any_data_example():
    """Testing filter with kwarg which is not in any data example"""
    assert not make_filter(some_arg='some_value').apply(sample_data)


def test_multiple_kwargs_from_different_data_examples():
    """Testing filter with different kwarg from different data examples"""
    assert not make_filter(kind='parrot', type='person').apply(sample_data)
