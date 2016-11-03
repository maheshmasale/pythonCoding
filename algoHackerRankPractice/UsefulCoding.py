#put all 0 in array at the end.
arr = [0,1,2,0,4, 3, 3, 2, 1]
originalLen = len(arr)
arr = [x for x in arr if x != 0]
arr = arr + [0 for x in range(originalLen - len(arr)) ]

#print(arr)


#Given a string find the next permutation string.
#t = int(input().strip())
str = "dkhc"
changeIndex = -1
for j in range(len(str)-1, 0, -1):
    if str[j] > str[j-1]:
        changeIndex = j-1
        print(changeIndex)
        for itr in range(len(str)-1,changeIndex,-1):
            if str[changeIndex] < str[itr]:
                print(itr)
                str = str[0:changeIndex] + str[itr] + str[changeIndex+1:itr] + str[changeIndex] + str[itr+1:]
                str = str[0:changeIndex+1] + "".join(sorted(list(str[changeIndex+1:])))
                break
        break
if changeIndex == -1:
    print("no answer")
else:
    print(str)



#Find whether the number is power of two?
sum([int(i) for i in '{0:b}'.format(6)]) > 1

#find the highest power of 2 below the given number.
b = 6

int( '1'.ljust(len('{0:b}'.format(b)),'0'),2)