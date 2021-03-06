# 29
'''Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
'''
def distinct_powers(a_range: tuple, b_range: tuple) -> int:
    powers = set([a**b for a in range(a_range[0], a_range[1]+1) for b in range(b_range[0], b_range[1]+ 1)])
    return len(powers)

# 30
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def digit_power_sum(power: int) -> int:
    fitting = [x for x in range(2,power*9**power) if sum(int(char)**power for char in str(x)) == x]
    return sum(fitting)

# 31
'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
def ways_to_target(target: int, coins: list) -> int:
    combinations = [1] +[0]*(target)
    for coin in coins:
        for i in range(coin,target +1):
            combinations[i] += combinations[i-coin]
    return combinations[target]
#32
def is_pandigital(i: int, j:int, limit: int) -> bool:
    return not bool('123456789'[0:limit].strip(f"{i}{j}{i*j}"))

def calulcate_pandigital_sum_to_lim(limit:int) -> int:
    products = set()
    for i in range(2,99):
        for j in range (i+1,9999//i):
            if is_pandigital(i,j,limit):
                logger.debug(f"{i} x {j} = {i*j}")
                products.add(i*j)
    return sum(products)


#33:
'''
Digit cancelling fractions
Submit

 Show HTML problem content 
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def non_trivial():
    list_nontrivial = [(i,j) for i in range(10,100) for j in range(i+1,100) if j%10 != 0 and str(i)[1]== str(j)[0] and float(i/j) == float(str(i)[0])/float(str(j)[1])]
    nom, denom = zip(*list_nontrivial)

    return str(Fraction(math.prod(nom), math.prod(denom)).denominator)

#34

def digit_factorials() -> int:
    factorials = [1]
    for i in range(1,10):
        factorials.append(reduce(lambda a,b: a*b,  range(1,i+1)))
    print(factorials)

    return sum(digit for digit in range(3,factorials[9]*9) if sum(factorials[int(digit)] for digit in str(digit)) == digit)


# 37
def truncatable_primes(limit: int) -> int:
    primes = [True for i in range(limit+1)]
    p=2

    while p**2 < limit:
        if(primes[p] == True):
            for x in range(p*2,limit+1,p):
                primes[x] = False
        p += 1
    primes[0] = False
    primes[1] = False

    gen = (i for i,x in enumerate(primes) if x and i > 11)
    prime_numbers = list(gen)
    count = 0
    sum =0
    while count < 11:
        for prime in prime_numbers:
            truncatable = True
            ends = all(primes[int(str(prime)[i:])] for i in range(len(str(prime))))
            beginnings = all(primes[int(str(prime)[:j])] for j in range(1,len(str(prime))))
            if ends and beginnings:
                print(prime)
                sum += prime
                count += 1

    return sum


#42 coded triangle numbers
def tri_words(word_list: list) ->int:
    triangles = [int((x*.5)*(x+1)) for x in itertools.takewhile(lambda x: (x*.5)*(x+1) < 2600, itertools.count())]
    letter_value = {}
    for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        letter_value[letter] = i+1
    return sum(1 for word in word_list if sum(map(lambda a: letter_value[a], word)) in triangles)
    # print(f"{word}{sum(map(lambda a: letter_value[a], list(word)))}")
