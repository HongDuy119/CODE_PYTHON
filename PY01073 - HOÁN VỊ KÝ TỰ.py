from itertools import permutations
from re import S


s = permutations(input())
for i in s:
    print("".join(i))
