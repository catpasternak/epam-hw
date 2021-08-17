"""
"Here's a not very efficient calculation function that calculates something important:

import time
import struct
import random
import hashlib

def slow_calculate(value):
    # Some weird voodoo magic calculations
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500. Calculation time
should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.

"""

import hashlib
import random
import struct
import time
from multiprocessing import Pool


def timer(func):
    """Decorator that counts function execution time"""

    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        stop = time.time()
        elapsed_time = stop - start
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return output

    return wrapper


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


@timer
def boosted_calculate_500():
    with Pool(32) as pool:
        answer = sum(pool.map(slow_calculate, list(range(500))))
    return answer


def time_of_boosted_calc_50():
    with Pool(8) as pool:
        start = time.time()
        answer = sum(pool.map(slow_calculate, list(range(50))))
        stop = time.time()
        elapsed_time = stop - start
    return elapsed_time
