def expressionTree(exprStr):
    exprArr = exprStr.split("/")
    expr = [i for i in exprArr[0] if i != " "]
    cmdLst = [i for i in exprArr[1] if i != " "]
    for i in cmdLst:
        if i == "S":
            expr = simplifyArr(expr)
        if i == "R":
            expr = reverseExpr(expr)

    return ''.join(expr)

def simplifyArr(expr):
    strOut = ""
    startInd = -1
    EndInd = -1
    varCnt = 0
    for i in range(len(expr)):
        if ord(expr[i]) == 40 and (varCnt % 3) == 0 and ord(expr[i+3])==41:
            startInd = i
            EndInd = i+3
            break
        if ord(expr[i]) >41:
                varCnt +=1
    for i in range(len(expr)):
        if not (i == startInd or i == EndInd):
            strOut += expr[i]
    expr = [i for i in strOut]
    if startInd > -1:
        expr =simplifyArr(expr)

    return expr

'''
def simplifyArr(expr):
    strOut = ""
    startOpenParenFlag = False
    cnt = 0
    varCnt = 0
    for i in range(len(expr)):
        if ord(expr[i]) == 40 and not startOpenParenFlag and (varCnt % 3) == 0:
            startOpenParenFlag = True
        elif ord(expr[i]) == 40 and startOpenParenFlag:
            strOut += expr[i]
            cnt += 1
        elif ord(expr[i]) == 41 and cnt == 0 and startOpenParenFlag:
            strOut += ''.join(expr[i+1:])
            break
        elif ord(expr[i]) == 41 and cnt != 0 and startOpenParenFlag:
            cnt -=1
            strOut += expr[i]
        else:
            varCnt += 1
            strOut += expr[i]
    print(strOut)
    return [i for i in strOut]
'''


def reverseExpr(expr):
    j = len(expr)-1
    i = 0
    dictParen = {")":"(","(":")"}

    while i < j:
        expr[i],expr[j] =expr[j],expr[i]
        if expr[i] in dictParen:
            expr[i] = dictParen[expr[i]]
        if expr[j] in dictParen:
            expr[j] = dictParen[expr[j]]
        i+=1
        j-=1

    return expr


print(expressionTree("(AB)C((DE)F)/SSSRR"))

