import math
from itertools import product

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
# 4 
max = 0
for i in range (100,1000):
    for j in range (100,1000):
        test = i*j
        if test == int(str(test)[::-1]) and test > max:
            max = test
logger.info(max)
# 5
from itertools import count
for i in count(20):
    if all(map(lambda divisor: i % divisor == 0, range(1, 21))):
        logger.info(i)
        break


# 6
logger.info(sum(map(lambda i : i**2, range (1,101)))-sum(range(1,101))**2)

# 7
count = 1
x = 3
while count < 10000:
    prime = True
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            prime = False
            break
    else:
        count = count + 1
    x = x + 2
logger.info(x)
 '''
# # 8
# max_product = 5832
# num = '''
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
# '''
# clean_string = num.replace("\n","")
# for index in range(len(clean_string)-13):
#     test = clean_string[index:index+13]
#
#     result = math.prod(list(map(lambda x: int(x),list(test))))
#     if int(result) > max_product:
#         max_product = result
# logger.info(max_product)
