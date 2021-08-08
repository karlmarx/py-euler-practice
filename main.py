import itertools
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


if __name__ == '__main__':
    with open("p042_words.txt","r") as f:
        string_list = sorted(list(map(lambda s: s[1:-1],f.read().split(","))))

    print(tri_words(string_list))

