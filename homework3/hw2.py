"""
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def estimate_time(value: int) -> int:
    """Calculate sum of slow function results with time_limit"""
    time_limit = 60
    start_time = time.time()
    attempts = 3
    for attempt in range(attempts):
        _ = slow_calculate(attempt)
    execution_time = (time.time() - start_time) / attempts
    approx_time = value * execution_time
    workers_need = max(1, int(approx_time // (time_limit/2)))

    i = 0
    while 2**i < workers_need:
        i += 1

    with Pool(2**i) as p:
        result = p.map(slow_calculate, list(range(value)))

    return sum(result)


if __name__ == '__main__':
    _ = estimate_time(501)
