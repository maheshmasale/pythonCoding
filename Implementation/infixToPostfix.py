def getPrecedense(charac):
    if charac == "+" or charac == "-":
        return 1
    if charac == "*" or charac == "/":
        return 2
    if charac == "^":
        return 3
    return -1


def isOperand(charac):
    if charac >= 'a' and charac <= "z" or charac >= 'A' and charac <= "Z" or charac >= '1' and charac <= "9":
        return True
    return False


def isValidExpr(expr):
    # validates whether the expression is valid or not
    return True


def infixToPrefix(exp):
    expr = list(exp)
    if not expr or len(expr) < 3:
        return expr

    if not isValidExpr(expr):
        return False

    tempStack = []
    k = -1
    for i in range(len(expr)):
        if isOperand(expr[i]):
            k += 1
            expr[k] = expr[i]
        elif expr[i] == "(":
            tempStack.append(expr[i])
        elif expr[i] == ")":
            while len(tempStack) > 0 and tempStack[-1] != "(":
                k = k + 1
                expr[k] = tempStack.pop()
            if len(tempStack) > 0 and tempStack[-1] != "(":
                return -1
            else:
                tempStack.pop()  # poping "(" character
        else:
            # operator case
            #print(expr[i],getPrecedense(expr[i]))
            while len(tempStack) > 0 and getPrecedense(expr[i]) <= getPrecedense(tempStack[-1]):
                k = k + 1
                expr[k] = tempStack.pop()
            tempStack.append(expr[i])
            #print(tempStack)
    while len(tempStack) > 0:
        k = k + 1
        expr[k] = tempStack.pop()
    expr = expr[:k+1]
    return "".join(expr)

def postFixEvaluate(exp):
    if not exp:
        return 0

    tempStack = []
    for i in range(len(exp)):
        if isOperand(exp[i]):
            tempStack.append(exp[i])
        else:
            num1 = tempStack.pop()
            num2 = tempStack.pop()
            if isOperand(num1) and isOperand(num2):
                tempNum = eval(str(num2)+exp[i]+str(num1))
                tempStack.append(tempNum)
            else:
                return "Error"
    return tempStack.pop()

#expr = "5+2*(2^3-4)^(4+1*5)-7"
expr = "5+4"
output = infixToPrefix(expr)
print(postFixEvaluate(output))


