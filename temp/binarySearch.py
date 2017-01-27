def bs(arr,trg):
    if not arr or len(arr) == 0:
        return -1

    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right + 1 )//2

        if arr[mid] > trg:
            right = mid - 1
        else:
            left = mid + 1

    if arr[right] == trg:
        return right

    return -1

print(bs([4,8,9,12],9))