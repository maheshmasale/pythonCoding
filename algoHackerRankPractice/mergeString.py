a= "zsd"
b="adwjfskfndkfjfnksadjnkdjnad"
def mergeStr(a,b):
    outputstr = ""
    if len(a) ==0:
        return b
    elif len(b) ==0:
        return a
    elif len(a) > len(b):
        for i in range(len(b)):
          outputstr = outputstr + a[i] + b[i]
        outputstr = outputstr + a[len(b):]
    else:
        for i in range(len(a)):
          outputstr = outputstr + a[i] + b[i]
        outputstr = outputstr + b[len(a):]
    return(outputstr)

print(mergeStr(a,b))