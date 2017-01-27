def kraken(m,n):
    paths = 0
    mat = [[-1 for i in range(n)] for i in range(m)]
    paths = krakenRecur(m,n,0,0,mat)
    return paths

def krakenRecur(m,n,i,j,mat):
    if not validCell(m,n,i,j):
        return 0
    if i == m-1 or j == n-1:
        return 1
    if mat[i][j] != -1:
        return mat[i][j]
    paths = krakenRecur(m,n,i+1,j+1,mat) + krakenRecur(m,n,i,j+1,mat) + krakenRecur(m,n,i+1,j,mat)
    mat[i][j] = paths
    return paths

def validCell(m,n,i,j):
    if i < m and j < n:
        return True
    return False

#print(kraken(400,400))
def krakenIter(m,n):
    paths = 0
    mat = [[-1 for i in range(n)] for i in range(m)]
    mat[m-1][n-1] = 1
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            #print(i,j)
            if j == n - 1 and i == m - 1:
                continue
            temp = 0
            if i != m-1:
                temp += mat[i+1][j]
            if j != n-1:
                temp += mat[i][j+1]
            if j != n - 1 and i != m - 1:
                temp += mat[i+1][j+1]
            mat[i][j] = temp
    return mat[0][0]

#[print("i-",i,",j-",j,"  ",krakenIter(i,j)) for i in range(1,7) for j in range(1,7)]


def krakenFormula(m,n):
    import math
    rum = 0
    f = math.factorial
    m-=1
    n-=1
    while m > 0 or n > 0:
        rum += f(m+n)/f(m)*f(n)
        m,n = m-1,n-1
    if not m and not n:
        rum +=1
    return int(rum)

#print(krakenFormula(3,3))

def  rearrangeWord(word):
    wordArr = [i for i in word]
    if word == None or len(wordArr) < 2:
        return 'no answer'
    i = len(wordArr)-2
    while i >=0 and wordArr[i] >= wordArr[i+1]:
        i -=1

    if i < 0:
        return 'no answer'
    if wordArr[i] == wordArr[len(wordArr)-1]:
        j = len(wordArr) - 1
        while (wordArr[j] == wordArr[i]):
            j -=1
        wordArr[i], wordArr[j] = wordArr[j], wordArr[i]
        wordArr = wordArr[0:i + 1] + sorted(wordArr[i + 1:])
    else:
        wordArr[i],wordArr[len(wordArr)-1] = wordArr[len(wordArr)-1],wordArr[i]
        wordArr = wordArr[0:i+1] + sorted(wordArr[i+1:])
    return "".join(wordArr)


def  buildSubsequencesWrongOne(s):
    sArr = list(s)
    subSequences = []
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            subSequences.append("".join(sArr[i:j]))
    return sorted(subSequences)


#print(buildSubsequences(str1))


def getSet(s):
    masks = [1<<i for i in range(len(s))]
    arrOut = []
    for i in range(2**len(s)):
        arrOut.append("".join([s[j] for j in range(len(s)) if (masks[j] & i)]))
    return sorted(arrOut)[1:]

str1 = "abc"
#print(getSet(str1))
