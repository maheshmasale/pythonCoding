def permutations(str1):
    arrStr = [i for i in str1]
    tempArr = []
    permu(arrStr,0,len(arrStr)-1,tempArr)
    return tempArr

def permu(arrStr,l,r,tempArr):
    if l == r:
        tempArr.append("".join(arrStr))
    else:
        for i in range(l,r+1):
            swap(arrStr,l,i)
            permu(arrStr,l+1,r,tempArr)
            swap(arrStr, l, i) #reverting changes

def swap(arrStr,l,i):
    if l == i:
        return arrStr
    arrStr[l],arrStr[i] = arrStr[i],arrStr[l]
    return arrStr

str1 ="ABcD"
arr1 =permutations(str1)
print(len(arr1))
print(len(set(arr1)))

