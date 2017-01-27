from numpy.distutils.system_info import gdk_info


def combinationSum3( k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    def check_combinations(results, current, n, k, path):
        if n < 0 or k < 0 or (n > 0 and k == 0):
            return
        if n == 0 and k == 0:
            results.append(path[:])
            return
        for x in range(current, 10):
            if n - x < 0:
                break

            path.append(x)
            check_combinations(results, x + 1, n - x, k - 1, path)
            path.pop()

        return results

    return check_combinations([], 1, n, k, [])

#print(combinationSum3(3,9))


def reverseWords(s):
    if s == None or s == "" or len(s) == 1 or s.strip() == "":
        return s
    sArr = s.split(" ")
    for i in range((len(sArr) // 2)+1):
        temp = sArr[i]
        sArr[i] = sArr[len(sArr) - 1 - i]
        sArr[len(sArr)-1 - i] = temp
    return " ".join(sArr)

#print(reverseWords(None))

def frequencySort(s):
    dictChar = {}
    for i in s:
        if i in dictChar:
            dictChar[i] += 1
        else:
            dictChar[i] = 1
    dictCharSorted = sorted(dictChar.items(), key=lambda x: x[1], reverse=True)

    strOut = ""
    for i in dictCharSorted:
        strOut += i[0] * i[1]
    return strOut


#print(frequencySort("aba"))




def getMedianFromTwoSortedArray(arrA,arrB):
    i = len(arrA) + len(arrB)
    a,b = 0,0
    finalArr = []
    while i > 0:
        if len(arrA)> a and len(arrB)> b :
            if arrA[a] < arrB[b]:
                finalArr.append(arrA[a])
                a+=1
            else:
                finalArr.append(arrB[b])
                b+=1
        elif len(arrA)> a:
            finalArr.extend(arrA[a:])
            break
        else:	#len(arrB)> b:
            finalArr.extend(arrB[b:])
            break
        i-=1

    print(finalArr)
    if len(finalArr) % 2 == 0:
        return (finalArr[len(finalArr)//2] + finalArr[len(finalArr)//2 + 1])/2
    else:
        return finalArr[len(finalArr)//2 + 1]

arrA = [1,5,7,9]
arrB = [2,3,4,5]
#print(getMedianFromTwoSortedArray(arrA,arrB))


def getMedianFromTwoSortedArr(arrA, arrB):
    print(arrA)
    print(arrB)
    if not len(arrA) > 0 and not len(arrB) > 0:
        return None
    elif len(arrA) > 0:
        m1 = arrA[len(arrA)//2] if len(arrA) % 2 != 0 else ((arrA[len(arrA)//2] + arrB[len(arrB)//2 - 1])/2)
    else:
        return m2
    if len(arrB) > 0:
        m2 = arrB[len(arrB)//2] if len(arrB) % 2 != 0 else ((arrB[len(arrB)//2] + arrB[len(arrB)//2 - 1])/2)
    else:
        return m1
    print(m1,m2)
    if m1 == m2:
        return m1
    elif m1 > m2:
        return getMedianFromTwoSortedArr(arrA[len(arrA)//2:], arrB[:len(arrA)//2-1])
    else:
        return getMedianFromTwoSortedArr(arrA[:len(arrA)//2-1], arrB[len(arrA)//2:])

#print(getMedianFromTwoSortedArr(arrA,arrB))




def getMedianFromSingleArr(arrA):
    if len(arrA) == 0:
        return None
    if len(arrA) % 2 == 0:
        return (arrA[len(arrA)//2]+arrA[len(arrA)//2-1])/2
    else:
        return arrA[len(arrA)//2]
arrA = [1,2,3]
#print(getMedianFromSingleArr(arrA))



str1 = "ABAB"
#str = "AABABBCACCC"
def getLongestSequenceAfterReplacement(str1,k):
    maxLength = 0
    dictChar = {}
    for i in range(len(str1)):
        if str1[i] in dictChar.keys():
            if str1[i] == str1[i-1]:
               dictChar[str1[i]]["countChars"][-1] += 1
            else:
                dictChar[str1[i]]["indexStack"].append(i)
                dictChar[str1[i]]["countChars"].append(1)
        else:
            dictCharTemp = {}
            dictCharTemp["indexStack"] = [i]
            dictCharTemp["countChars"] = [1]
            dictChar[str1[i]] = dictCharTemp
    #print(dictChar)
    for key in dictChar.keys():
        indexStack = dictChar[key]["indexStack"]
        countStack = dictChar[key]["countChars"]
        while(len(indexStack)>1):
            tpIndex = indexStack.pop()
            cntIndex = countStack.pop()

            tpPeek = indexStack[-1] #if len(indexStack) > 0 else []
            cntPeek = countStack[-1] #if len(countStack) > 0 else []

            #print(tpIndex, cntIndex, tpPeek, cntPeek)

            charsToBeReplaced = tpIndex - tpPeek - cntPeek
            sequenceLength = tpIndex + cntIndex - tpPeek
            #print(charsToBeReplaced, sequenceLength)
            if charsToBeReplaced <= k and maxLength < (sequenceLength + k-charsToBeReplaced):
                maxLength = sequenceLength + k - charsToBeReplaced

    return maxLength
#print(getLongestSequenceAfterReplacement(str1,3))


def testRandom():
    import random
    outcomes = { 'heads':0,
             'tails':0,
             }
    sides = list(outcomes.keys())
    for i in range(1000):
        outcomes[random.choice(sides)] += 1

    print('Heads:', outcomes['heads'])
    print('Tails:', outcomes['tails'])

#testRandom()

def generateGenderRatio(num):
    #ctci question 6.7
    girls = 0
    boys = 0

    for i in range(num):
        children = getChild()
        girls += children[0]
        boys += children[1]

    return girls/(girls+boys)



def getChild():
    girls = 0
    boys = 0

    import random

    while girls == 0:
        r = random.randint(0,1)
        if r:
            boys += 1
        else:
            girls += 1
    return [girls ,boys]

#print(generateGenderRatio(5))


def getUniqueNumer(nums):
    from operator import xor
    from functools import reduce
    return reduce(xor,nums)


#print(getUniqueNumer([5,4,5,8,4]))



def getSum(a, b):
    import math
    return int(math.log((2 ** a) * (2 ** b), 2))

#print(getSum(2147483647, -2147483648))



def addDigits(num):
    from functools import reduce
    numStr = str(num)
    f = lambda a, b: int(a) + int(b)
    while len(numStr) > 1:
        sumOfElem = reduce(f, numStr)
        numStr = str(sumOfElem)
    return int(numStr[0])

#print(addDigits(128))


def findTheDifference_bruteForce(s, t):
    sArr = [i for i in s]
    tArr = [i for i in t]
    for i in sArr:
        ind = tArr.index(i)
        del tArr[ind]
    return tArr[0]


def findTheDifference_dictionary(s, t):
    dictChars = {}
    for j in range(len(t)):
        if j < len(s):
            dictChars = increaseDicElem(dictChars,s[j])
        dictChars = decreaseDicElem(dictChars, t[j])

    return [arr[0] for arr in dictChars.items() if arr[1] < 0][0]
    #return t

def increaseDicElem(dict,elem):
    if not elem in dict:
       dict[elem] = 0
    dict[elem] += 1
    return dict

def decreaseDicElem(dict,elem):
    if not elem in dict:
       dict[elem] = 0
    dict[elem] -= 1
    return dict

def findTheDifference_elegantSolution(s,t):
    from functools import reduce
    from operator import xor
    return chr(reduce(xor,map(ord,s+t)))

#print(findTheDifference_dictionary("abcd","eabcd"))

#Code to get excel column number from given column name
def titleToNumber(s):
    from functools import reduce
    return reduce(lambda i, j: i + j, map(lambda arr: arr[1] * 26 ** arr[0], [[i, j] for i, j in enumerate(
        map(lambda x: ord(x) - 64, [s[i] for i in range(len(s) - 1, -1, -1)]))]))


def firstUniqChar(s):
    from functools import reduce
    dictChars = {}
    for i in range(len(s)):
        if s[i] not in dictChars:
            dictChars[s[i]] = {"iStart": i, "count": 0}
        dictChars[s[i]]["count"] += 1
    ftr = filter(lambda x: dictChars[x[0]]["count"] == 1, dictChars.items())
    iStart = (reduce(lambda x, y: x if x[1]["iStart"]<y[1]["iStart"] else y ,ftr))
    if iStart == None:
        return -1
    return iStart

#print(firstUniqChar("leetl"))

def isAnagram(s,t):
    from functools import reduce
    if not s and not t:
        return True

    if (not s and t) or (s and not t):
        return False

    sum_S = reduce(lambda x, y: x + y, [ord(i) for i in s])
    mul_S = reduce(lambda x, y: x * y, [ord(i) for i in s])
    sum_T = reduce(lambda x, y: x + y, [ord(i) for i in t])
    mul_T = reduce(lambda x, y: x * y, [ord(i) for i in t])
    print(sum_S,sum_T,mul_S,mul_T)
    return sum_S == sum_T and mul_S == mul_T

#print(isAnagram('ba','ab'))


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    from collections import Counter
    cntr = Counter(s)
    pallindromeLength = 0
    for i in cntr.items():
        if not i[1] % 2:
            pallindromeLength += i[1]
        else:
            pallindromeLength += i[1] - i[1]%2
    if pallindromeLength < len(s):
        pallindromeLength += 1
    return pallindromeLength

#print(longestPalindrome("abccccdd"))

