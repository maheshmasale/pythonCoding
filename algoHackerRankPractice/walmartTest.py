'''
#https://www.hackerrank.com/contests/walmart-codesprint-algo/challenges/emma-and-her-camera
#1st code

n =  int(input().strip())
x =  int(input().strip())
import math

totalCombo = sum([ int(math.factorial(n)/(math.factorial(n-i)*math.factorial(i))) for i in range(n)])
print(abs(totalCombo-x))

'''

