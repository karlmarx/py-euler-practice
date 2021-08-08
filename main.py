import math
import timeit
from collections import deque
from fractions import Fraction
from functools import reduce
from itertools import product
from typing import Deque, List

from loguru import logger
from functools import reduce
# project euler
# 34



def digit_factorials():
    factorials = [1]
    for i in range(1,10):
        factorials.append(reduce(lambda a,b: a*b,  range(1,i+1)))
    print(factorials)

    return sum(digit for digit in range(3,factorials[9]*9) if sum(factorials[int(digit)] for digit in str(digit)) == digit)


if __name__ == '__main__':
    logger.info(digit_factorials())