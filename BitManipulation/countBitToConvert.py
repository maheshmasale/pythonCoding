def countDifferentBits(num1, num2):
    count = 0
    while (num1 != 0 or num2!=0):
        if num1 == 0:
            if num2 & 1:
                count =count + 1
            num2 = num2 >> 1
        elif num2 ==0:
            if num1 & 1:
                count +=1
            num1 = num1 >> 1
        elif (num1 & 1) != (num2 & 1):
            count +=1
            num1 = num1 >> 1
            num2 = num2 >> 1
        else:
            num1 = num1 >> 1
            num2 = num2 >> 1
    return count

def countDifferentBits_best(a,b):
    count = 0
    c = a^b
    while c != 0:
        count += 1
        c = c & (c-1)
    return count

print(countDifferentBits(9,0))
print(countDifferentBits_best(9,0))

