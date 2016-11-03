import time

g_numberOfScalarMulti = 0
g_numberOfOptimalMulti = 0
g_numberOfRecursiveCalls = 0

def recursiveFindMatixMulti(d,i,j):
    global g_numberOfScalarMulti
    global g_numberOfRecursiveCalls
    if i == j:
        return 0
    elif  i > j:
        return 0
    else:
        l_optimalMulti = float("inf")
        tempMulti = 0
        for k in range(i, j):
            tempMulti = recursiveFindMatixMulti(d, i, k) + recursiveFindMatixMulti(d, k + 1, j) + d[i] * d[k + 1] * d[j + 1]

            g_numberOfScalarMulti = g_numberOfScalarMulti + 2
            g_numberOfRecursiveCalls = g_numberOfRecursiveCalls + 2

            if tempMulti < l_optimalMulti:
                l_optimalMulti = tempMulti
                matrixTable[i][j] = k

        return l_optimalMulti

def printOptimalParenthisations(l_matrixTable, i , j):
    if i == j:
        print("A"+str(i+1), end="")
    else:
        print("(", end="")
        printOptimalParenthisations(l_matrixTable,i,l_matrixTable[i][j] )
        printOptimalParenthisations(l_matrixTable, l_matrixTable[i][j] + 1, j)
        print(")", end="")



dimArr = [5, 2, 4, 7, 3, 9, 7, 8, 6, 3, 7, 5, 5]

time1 = time.clock()
matrixTable = [list(0 for i in range(len(dimArr))) for j in range(len(dimArr))]
numberOfOptimalMulti = recursiveFindMatixMulti(dimArr, 0, len(dimArr)-2)
print("Optimal parenthesization :")
printOptimalParenthisations(matrixTable, 0, len(dimArr)-2)
time2 = time.clock()

print("")
print("Optimal number of multplications required : ", numberOfOptimalMulti )
print("Number of scalar multiplications : ",g_numberOfScalarMulti)
print("Number of recursive calls made : ",g_numberOfRecursiveCalls)
timeDifference = 1000*(float(time2) - float(time1))
print("Total running time required : ", timeDifference)


'''
Output: -

Case 1 =
dimArr = [4,8,45,75,44,11,35,65]
Optimal parenthesization :
((((((A1A2)A3)A4)A5)A6)A7)
Optimal number of multplications required :  40716
Number of scalar multiplications :  728
Number of recursive calls made :  728
Total running time required :  1.02527

Case 2 =
dimArr = [25, 106, 44, 8, 17, 19, 17, 18, 60, 90, 3, 7, 6, 5]
Optimal parenthesization :
((A1(A2(A3(A4(A5(A6(A7(A8(A9A10)))))))))((A11A12)A13))
Optimal number of multplications required :  46293
Number of scalar multiplications :  531440
Number of recursive calls made :  531440
Total running time required :  527.99528

Case 3 =
dimArr = [5, 2, 4, 7, 3, 9, 7, 8, 6, 3, 7, 5, 5]
Optimal parenthesization :
(A1((((((((((A2A3)A4)A5)A6)A7)A8)A9)A10)A11)A12))
Optimal number of multplications required :  734
Number of scalar multiplications :  177146
Number of recursive calls made :  177146
Total running time required :  208.65774

'''