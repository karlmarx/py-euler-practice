import math
import timeit
from functools import reduce
from itertools import product

from loguru import logger
from functools import reduce
# project euler


def fibonacci_to_length(num_digits: int):
    # count = 0
    numbers = (0,1)
    while len(str(numbers[1])) < num_digits:
        new = sum(numbers)
        numbers = (numbers[1], new)
        print(numbers)




if __name__ == '__main__':
    logger.info(fibonacci_to_length(1000))