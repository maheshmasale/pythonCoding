def reverseStrOnly(strInp):
    strArr = [i for i in strInp]
    #return " ".join(list(map(lambda x: "".join(list(reversed(x))),str1.split(' '))))
    print(" ".join(list(map(lambda x: "".join(list(reversed(x))),str1.split(' ')))))
    i,j = 0,0
    while j < len(strArr):
        if strArr[j] == " ":
            strArr = getPartiallyReversed(strArr,i,j-1)
            j += 1
            i = j
        else:
            j+=1

    return "".join(strArr)

def getPartiallyReversed(strArr,i,j):
    while i < j:
        strArr[i], strArr[j] = strArr[j], strArr[i]
        i += 1
        j -= 1
    return strArr

str1 = "The      News Is Not      true   "
print(reverseStrOnly(str1))