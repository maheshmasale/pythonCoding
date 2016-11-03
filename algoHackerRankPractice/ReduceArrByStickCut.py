arr = [0,1,2,3,4, 3, 3, 2, 1]
arr = [x for x in arr if x > 0]
while len(arr) > 0:
    arr = sorted(arr)
    print(len(arr))
    minArr = arr[0]
    arr = [x for x in arr if x > minArr]
