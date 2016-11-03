import time

g_numberOfScalarMulti = 0
g_numberOfOptimalMulti = 0
g_numberOfRecursiveCalls = 0

def memoizedFindMatixMulti(d,i,j):
    global g_numberOfScalarMulti
    global g_numberOfRecursiveCalls
    global g_valMultiMatrixTable
    if i == j:
        return 0
    elif  i > j:
        return 0
    elif g_valMultiMatrixTable[i][j] < float("inf"):
        return g_valMultiMatrixTable[i][j]
    else:
        tempMulti = 0
        for k in range(i, j):
            tempMulti = memoizedFindMatixMulti(d, i, k) + memoizedFindMatixMulti(d, k + 1, j) + d[i] * d[k + 1] * d[j + 1]

            g_numberOfScalarMulti = g_numberOfScalarMulti + 2
            g_numberOfRecursiveCalls = g_numberOfRecursiveCalls + 2

            if tempMulti < g_valMultiMatrixTable[i][j]:
                g_valMultiMatrixTable[i][j] = tempMulti
                matrixTable[i][j] = k

        return g_valMultiMatrixTable[i][j]

def printOptimalParenthisations(l_matrixTable, i , j):
    if i == j:
        print("A"+str(i+1), end="")
    else:
        print("(", end="")
        printOptimalParenthisations(l_matrixTable,i,l_matrixTable[i][j] )
        printOptimalParenthisations(l_matrixTable, l_matrixTable[i][j] + 1, j)
        print(")", end="")



dimArr = [4,8,45,75,44,11,35,65]

time1 = time.clock()
matrixTable = [list(0 for i in range(len(dimArr))) for j in range(len(dimArr))]
g_valMultiMatrixTable = [list(float("inf") for i in range(len(dimArr))) for j in range(len(dimArr))]
numberOfOptimalMulti = memoizedFindMatixMulti(dimArr, 0, len(dimArr)-2)
print("Optimal parenthesization :")
printOptimalParenthisations(matrixTable, 0, len(dimArr)-2)
time2 = time.clock()

print("")
print("Optimal number of multplications required : ", numberOfOptimalMulti )
print("Number of scalar multiplications : ",g_numberOfScalarMulti)
print("Number of recursive calls made : ",g_numberOfRecursiveCalls)
timeDifference = 1000* (float(time2) - float(time1))
print("Total running time required : ", timeDifference)


'''
Output: -

Case 1 =
dimArr = [4,8,45,75,44,11,35,65]
Optimal parenthesization :
((((((A1A2)A3)A4)A5)A6)A7)
Optimal number of multplications required :  40716
Number of scalar multiplications :  112
Number of recursive calls made :  112
Total running time required :  0.35839

Case 2 =
dimArr = [25, 106, 44, 8, 17, 19, 17, 18, 60, 90, 3, 7, 6, 5]
Optimal parenthesization :
((A1(A2(A3(A4(A5(A6(A7(A8(A9A10)))))))))((A11A12)A13))
Optimal number of multplications required :  46293
Number of scalar multiplications :  728
Number of recursive calls made :  728
Total running time required :  1.49461

Case 3 =
dimArr = [5, 2, 4, 7, 3, 9, 7, 8, 6, 3, 7, 5, 5]
Optimal parenthesization :
(A1((((((((((A2A3)A4)A5)A6)A7)A8)A9)A10)A11)A12))
Optimal number of multplications required :  734
Number of scalar multiplications :  572
Number of recursive calls made :  572
Total running time required :  0.78975

'''