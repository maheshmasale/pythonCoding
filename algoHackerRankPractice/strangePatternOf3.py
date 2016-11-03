#https://www.hackerrank.com/challenges/strange-code
'''
t = 1582
s = 3
n = 1
while n < t:
    n = n + s
    s = 2 * s
#print(n,s)
if n == t:
    print(s)
else:
    s = s//2
    n = n - s
    s = s - t + n
    #print(n,t,s)
    print(s)

'''




#https://www.hackerrank.com/challenges/flatland-space-stations?h_r=next-challenge&h_v=zen


n = 99989
m = 4
c = [int(c_temp) for c_temp in "75453 36129 64502 46817".split(' ')]
if n == m:
    print(0)
else:
    c = sorted(c)
    print(c)
    maxDistance = 0
    for i in range(len(c)-1):
        if (c[i+1] - c[i]) > maxDistance:
            maxDistance = c[i+1] - c[i]
    maxDistance = maxDistance//2
    if maxDistance < n-1-c[m-1]:
        maxDistance = n-1-c[m-1]
    if maxDistance < c[0]:
        maxDistance = c[0]

print(maxDistance)