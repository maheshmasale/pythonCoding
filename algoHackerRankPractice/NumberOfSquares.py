#https://www.hackerrank.com/challenges/sherlock-and-squares

import math
cases = int(input().strip())
for i in range(cases):
    x,y = input().strip().split()
    x = int(x)
    y = int(y)
    x = x**(0.5)
    y = y**(0.5)
    #print("x:",x,"   y:",y)
    x = math.ceil(x)
    y = math.floor(y)
    #print("x:",x,"   y:",y)
    if x<y:
        print(y-x+1)
    elif x==y:
        print(1)
    else:
        print(0)