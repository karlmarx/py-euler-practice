import math

from loguru import logger
# project euler
'''
# 1
sum = 0

for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x
logger.info(f"sum={sum}")

# 2
x,y = (1,2)
sum = 0
while (x < 4000000 and y < 4000000):
    if (x % 2 == 0):
        sum = sum + x
    if (y % 2 == 0):
        sum = sum + y
    x = x + y
    y= x + y
logger.info(f"sum={sum}")

# 3
n = 600851475143
largest = 2
while n % 2 == 0:
    n = n /2

for i in range(3, int(math.sqrt(n))+1, 2):
    while n % i == 0:
        if i > largest:
            largest = i
        n = n / i

if n > 2:
    largest = n
logger.info(largest)
 4 
max = 0
for i in range (100,1000):
    for j in range (100,1000):
        test = i*j
        if test == int(str(test)[::-1]) and test > max:
            max = test
logger.info(max)
'''
# 5
from itertools import count
for i in count(20):
    if all(map(lambda divisor: i % divisor == 0, range(1, 21))):
        logger.info(i)
        break


