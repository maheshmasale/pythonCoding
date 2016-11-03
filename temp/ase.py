mat = [[0,1,-1],[1,0,-1],[1,1,1]]


def startit(mat):
    currentpos = [0,0]
    return round(mat,currentpos,"up") + round(mat,currentpos,"down")

def round(mat,currentpos,directionStr):
   if directionStr == "up":
       if currentpos[0] + 1 > len(mat) - 1:
           return 0
       elif currentpos[1] + 1 > len(mat[0]) - 1:
           return 0
       elif mat[currentpos[0]][currentpos[1]+1] == -1:
            count = 0
            if mat[currentpos[0]+1][currentpos[1]] == 1:
                mat[currentpos[0]+1][currentpos[1]] = 0
                count = 1
            print(currentpos, round(mat, list([currentpos[0] + 1, currentpos[1]]), directionStr))
            return count + round(mat,list([currentpos[0]+1,currentpos[1]]),directionStr)

       elif mat[currentpos[0]+1][currentpos[1]] == -1:
            count = 0
            if mat[currentpos[0]][currentpos[1]+1] == 1:
                mat[currentpos[0]][currentpos[1]+1] = 0
                count = 1
            print(currentpos, round(mat, list([currentpos[0], currentpos[1]+1]), directionStr))
            return count + round(mat, list([currentpos[0], currentpos[1]+1]), directionStr)

       else:
            count1,count2 = 0,0
            if mat[currentpos[0]][currentpos[1] + 1] == 1:
                mat[currentpos[0]][currentpos[1] + 1] = 0
                count1 = count1 + 1
                count1 = count1 + round(mat, list([currentpos[0], currentpos[1]+1]), directionStr)

            if mat[currentpos[0]+1][currentpos[1]] == 1:
                mat[currentpos[0]+1][currentpos[1]] = 0
                count2 = count2 + 1
                count2 = count2 + round(mat,list([currentpos[0]+1,currentpos[1]]),directionStr)
            print(currentpos, count1,count2)
            return max(count1,count2)

   else:
       if currentpos[0] - 1 > - 1:
           return 0
       elif currentpos[1] - 1 > - 1:
           return 0
       elif mat[currentpos[0]][currentpos[1] - 1] == -1:
            count = 0
            if mat[currentpos[0] - 1][currentpos[1]] == 1:
                mat[currentpos[0] - 1][currentpos[1]] = 0
                count = 1
            return count + round(mat, list([currentpos[0] - 1, currentpos[1]]), directionStr)

       elif mat[currentpos[0] - 1][currentpos[1]] == -1:
            count = 0
            if mat[currentpos[0]][currentpos[1] - 1] == 1:
                mat[currentpos[0]][currentpos[1] - 1] = 0
                count = 1
            return count + round(mat, list([currentpos[0], currentpos[1] - 1]), directionStr)

       else:
            count1, count2 = 0, 0
            if mat[currentpos[0]][currentpos[1] - 1] == 1:
                mat[currentpos[0]][currentpos[1] - 1] = 0
                count1 = count1 + 1
                count1 = count1 + round(mat, list([currentpos[0], currentpos[1] - 1]), directionStr)

            if mat[currentpos[0] - 1][currentpos[1]] == 1:
                mat[currentpos[0] - 1][currentpos[1]] = 0
                count2 = count2 + 1
                count2 = count2 + round(mat, list([currentpos[0] - 1, currentpos[1]]), directionStr)
            return max(count1, count2)


print(startit(mat))