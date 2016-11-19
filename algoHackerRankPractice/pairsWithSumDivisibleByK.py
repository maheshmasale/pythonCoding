#https://www.hackerrank.com/challenges/linkedin-practice-divisible-sum-pairs

def getCountOfPairs(n, k, a):
    dicModArr = {}
    countPairs = 0
    for i in range(n):
        if (k - a[i] % k) % k in dicModArr:
            countPairs += dicModArr[(k - a[i] % k) % k]
        if a[i] % k not in dicModArr:
            dicModArr[a[i] % k] = 1
        else:
            dicModArr[a[i] % k] += 1

    print(countPairs)

getCountOfPairs(6,3, [1, 3, 2, 6, 1, 2])