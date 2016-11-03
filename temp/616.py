n = 4
k = 4
arr = list([6,7, 2, 4])
dic = {}
if k==0:
    print(len(arr))
else:
    for i in arr:
        if i%k in dic:
            dic[i%k].append(i)
        else:
            dic[i%k] = list()
            dic[i%k].append(i)

    count = 0
    for i in range(1, k//2 + 1):
        if i in dic:
            if k-i in dic:
                if i != k-i:
                    if len(dic[i]) > len(dic[k - i]):
                        count = count + len(dic[i])
                    else:
                        count = count + len(dic[k-i])
            else:
                count = count + len(dic[i])
        else:
            if k-i in dic:
                count = count + len(dic[k-i])

    if 0 in dic:
        count = count + min(len(dic[0]),1)
    if k%2 == 0:
        if k//2 in dic:
            count = count + min(len(dic[k//2]), 1)

#print(dic)
#print(count)

s = "abc"
n = 100
count = 0
for i in s:
    if i == 'a':
        count += 1

if len(s) < n:
    count = count * (n // len(s))
    for i in range(n%len(s)):
        if s[i] == 'a':
            count += 1

print(count)