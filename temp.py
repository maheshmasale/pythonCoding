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



str = "ABAB"
#str = "AABABBCACCC"
def getLongestSequenceAfterReplacement(str,k):
    maxLength = 0
    dictChar = {}
    for i in range(len(str)):
        if str[i] in dictChar.keys():
            if str[i] == str[i-1]:
               dictChar[str[i]]["countChars"][-1] += 1
            else:
                dictChar[str[i]]["indexStack"].append(i)
                dictChar[str[i]]["countChars"].append(1)
        else:
            dictCharTemp = {}
            dictCharTemp["indexStack"] = [i]
            dictCharTemp["countChars"] = [1]
            dictChar[str[i]] = dictCharTemp
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
#print(getLongestSequenceAfterReplacement(str,3))


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


print(getUniqueNumer([5,4,5,8,4]))