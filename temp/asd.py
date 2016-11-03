ar = [-2,4,-6,0,7,0,-5,4]
n = 8
neg,pos,sero = 0,0,0
import numbers
for i in range(n):
    if ar[i] == 0:
        sero = sero +1
    elif ar[i] < 0:
        neg = neg + 1
    else:
        pos = pos + 1

print(pos/n,6)
print(neg/n)
print(sero/n)
