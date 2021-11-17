"""
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""
import hashlib
import os
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def parallelize_calculations(value: int) -> int:
    """
    Parallelize calculation of sum of slow function results
    to meet the time limit
    """
    time_limit = 60  # Set time limit
    # Calculate average time of one function call
    start_time = time.time()
    attempts = 3
    for attempt in range(attempts):
        _ = slow_calculate(attempt)
    execution_time = (time.time() - start_time) / attempts
    # Estimate approximate workers number
    approx_time = value * execution_time
    workers_need = max(1, int(approx_time // (time_limit/2)))

    cpu_number = os.cpu_count()
    # Take first multiplication coefficient for cpu_number that
    # is greater or equal then workers_need
    i = 1
    while cpu_number*i < workers_need:
        i += 1

    with Pool(cpu_number*i) as p:
        result = p.map(slow_calculate, list(range(value)))

    return sum(result)
