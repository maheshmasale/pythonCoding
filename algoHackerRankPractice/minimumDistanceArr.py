##https://www.hackerrank.com/challenges/minimum-distances
'''
A = [int(A_temp) for A_temp in "7 1 3 4 1 7".split(' ')]
arrVal = list()
arrSeq = list()
for count, elem in enumerate(A):
    arrSeq.append(count)
    arrVal.append(elem)

print(zipped = zip(arrSeq,arrVal))
print(sorted(zipped))

'''
#!/bin/python3

import sys


n = 6
A = [int(A_temp) for A_temp in '7 1 3 4 1 7'.strip().split(' ')]
d=n
count = 0
for i in range(n):
    j=1
    while(i-j>-1 or i+j < n and j < d):
        if i-j>-1:
            if A[i-j] == A[i] and j < d:
                print(j)
                d = j
        if i+j < n:
            print('in more')
            if A[i+j] == A[i] and j < d:
                d = j
        j = j + 1

if d==n:
    print(-1)
else:
    print(d)


