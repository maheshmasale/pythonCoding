n = 4
a = [1,2,3,4]

totalsum = 0
if n == 0:
    print(0)
for i in range(len(a)-1):
    a = sorted(a)
    print(a)
    sum1 = a[0]+a[1]
    totalsum = totalsum + sum1
    a = a[2:]
    a.append(sum1)

print(totalsum)

