def decimalToBinary(num):
    if num > 1 or num < 0:
        return "ERROR"
    binaryStr = "."
    while num > 0:
        if len(binaryStr) == 32:
            return "ERROR"

        r = num * 2
        if r >= 1:
            binaryStr += "1"
            num = r - 1
        else:
            binaryStr += "0"
            num = r

    return binaryStr


print(decimalToBinary(0.72))