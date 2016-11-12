class Solution(object):
    def getPermutation(self, globalArr, k, n, start, prefixArr):

        if k == 1:
            if n > start and n<10:

                if prefixArr == None:
                    prefixArr = [n]
                else:
                    prefixArr.append(n)
                if globalArr == None:
                    globalArr = [prefixArr]
                else:
                    globalArr.append(prefixArr)
            else:
                return

        else:
            for i in range(start, 10):
                tempFix = []
                tempFix.extend(prefixArr)
                if tempFix == None:
                    tempFix = [i]
                else:
                    tempFix.append(i)
                self.getPermutation(globalArr, k - 1, n - i, i + 1, tempFix)

    def combinationSum3(self, k, n):
        globalArr = []
        prefixArr = []
        self.getPermutation(globalArr, k, n, 1, prefixArr)
        return globalArr



g = Solution()
arr = g.combinationSum3(3,7)
print(arr)