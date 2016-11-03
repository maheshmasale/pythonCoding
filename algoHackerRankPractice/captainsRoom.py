k = 5
arr = list(map(int,'1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 '.split()))
sumArr = sum(arr)
idealSum = 0
dic_Data = {"temp":"as"}
for i in range(len(arr)):
    if not arr[i] in dic_Data:
        dic_Data[arr[i]] = arr[i]
        idealSum += arr[i] * k

print(int((idealSum - sumArr)/(k-1)))