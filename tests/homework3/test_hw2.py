import time

from homework3.hw2 import parallelize_calculations


def test_calculations_time():
    """Assert that running time is less then 60 secs"""
    start_time = time.time()
    time_limit = 60

    parallelize_calculations(501)

    end_time = time.time()
    result_time = end_time - start_time

    assert result_time < time_limit
