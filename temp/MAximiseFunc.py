#https://www.hackerrank.com/challenges/maximize-it
from itertools import product
N, M = [int(x) for x in input().strip().split()]
arrN = list()
for j in range(N):
    arrN.append([int(i) for i in input().strip().split()][1:])

allCombo = list(product(*arrN))

def func(nums):
    return sum(x*x for x in nums) % M

print(max(list(map(func, allCombo))))