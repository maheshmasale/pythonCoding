n = 512

for i in range(len(arr)):
    if arr[i] not in arr[i+1:]:
        print(arr[i])
        break


