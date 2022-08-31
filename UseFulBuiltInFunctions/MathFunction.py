from ast import Pow
from pstats import SortKey
import math
import statistics
import itertools


pow(2, 5)
abs(-50)
round(1.22)

points = [0,212,2332,1231,3242,12313,1231,23454647,3452234123]

points.sort()

print(math.pi)

math.factorial(4)
math.sqrt(18)
math.gcd(8,12)

ageData = [10,13,14,12,11,10,15]
statistics.mode(ageData)
statistics.mean(ageData)

for x in itertools.count():
    print(x)
    if x == 60:
        break;
