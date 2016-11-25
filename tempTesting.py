
def weave(lArr,rArr, prefix,permuArr = []):
    #use recursion to find the permutations of given sequence by keeping the sequence intact.
    tempPrefix = []
    tempPrefix.extend(prefix)
    if len(lArr) ==0 or len(rArr) == 0:
        tempPrefix.extend(lArr)
        tempPrefix.extend(rArr)
        permuArr.append(tempPrefix)
        return permuArr

    tempPrefix.append(lArr[0])
    weave(lArr[1:],rArr,tempPrefix,permuArr)
    tempPrefix.pop()
    tempPrefix.append(rArr[0])
    weave(lArr,rArr[1:], tempPrefix ,permuArr)
    tempPrefix.pop()
    return permuArr

#permutationsArr = weave(["a","b","c"],["d","e","f"],"",[])
#permutationsArr = weave(["a","b"],["d","e"],"",[])
#print(permutationsArr)


def getKMPArr(str1):
    arrKMP = [0]*len(str1)
    i = 0
    j = i + 1
    while j < len(str1):
        if str1[i]==str1[j]:
            arrKMP[j] = arrKMP[j-1]+1
            i+=1
            j+=1
        else:
            i = 0
            if str1[i] == str1[j]:
                arrKMP[j] = 1
                i += 1
            else:
                arrKMP[j] = 0
            j += 1
    return arrKMP

def getKMPArr_better(str1):
    arrKMP = [0]*len(str1)
    i = 0
    j = i + 1
    while j < len(str1):
        if str1[i]==str1[j]:
            arrKMP[j] = i+1
            i+=1
            j+=1
        else:
            i = 0
            if str1[i] == str1[j]:
                arrKMP[j] = i + 1
                i += 1
            j = j+1
    return arrKMP

#print(getKMPArr_better("aabaabaaa"))



def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

#print(["".join(i) for i in permutations("ABCD",2)])


def repeatedSubstringPattern(str1):
    if not str1 or len(str1) < 2:
        return False
    for i in range(1, (len(str1) // 2) +1):
        if not len(str1) % i:
            tempStr = ""
            subStr = str1[0:i]
            for j in range(len(str1) // i):
                tempStr += subStr
            if tempStr == str1:
                return True
    return False

#print(repeatedSubstringPattern("abab"))

count = 0
def countSteps(n):
    global count
    countRecurse(n)
    return count


def countRecurse(n):
    global count
    if n == 0:
        count+=1
    if n-1 >= 0:
        countRecurse(n-1)
    if n-2 >= 0:
        countRecurse(n-2)
    if n-3 >= 0:
        countRecurse(n-3)


def countSteps_iter(n):
    if n < 3:
        return n
    a,b,c = 1,2,4

    for i in range(4, n+1):
        a, b, c = b, c, a+b+c
    return c


print(countSteps(5))
print(countSteps_iter(5))