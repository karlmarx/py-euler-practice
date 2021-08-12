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
# # 48 Self factors to
#
# def self_powers_to(limit: int) -> int:
#     list = [x**x for x in range(1,10)]
#     return sum(list)
#
# def test_powers():
#     result = self_powers_to(3)
#     assert result == 3
def fibo_bottom_up(n: int) -> int:
    a = 1
    b = 1
    for i in range (2,n+1):
        a,b = b, a + b
    return b


if __name__ == '__main__':
    sdf = [*map(lambda a: print(str(fibo_bottom_up(a))), range(1,20))]



    # with open("p042_words.txt","r") as f:
    #     string_list = sorted(list(map(lambda s: s[1:-1],f.read().split(","))))
    #
    # print(tri_words(string_list))

