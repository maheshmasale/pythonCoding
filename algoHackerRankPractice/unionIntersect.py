from _sre import getlower
from cmath import sqrt

from __builtin__ import abs

n = 4
arrInt = [5,2,3,6,8,6]

arrInt = sorted(arrInt, reverse = True)
for i in range(len(arrInt)-2):
    if arrInt[i] < arrInt[i+1] + arrInt[i+2]:
        print(arrInt[i+2], arrInt[i+1],arrInt[i] )
        break
