#https://www.hackerrank.com/challenges/almost-sorted
n = int(input().strip())
arr = [int(i) for i in input().strip().split()]
counter = []
countinuous = True
for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        counter.append(i)
        if len(counter) > 1 and counter[len(counter) - 2] != i - 1:
            countinuous = False

if len(counter) == 1:
    arr[counter[0]], arr[counter[0] + 1] = arr[counter[0] + 1], arr[counter[0]]
    temparr = sorted(arr)
    if temparr == arr:
        print("yes")
        print("swap", counter[0] + 1, counter[0] + 2)
    else:
        print("no")
elif len(counter) == 2:
    arr[counter[0]], arr[counter[1] + 1] = arr[counter[1] + 1], arr[counter[0]]
    print("yes")
    print("swap", counter[0] + 1, counter[1] + 2)
elif len(counter) > 2 and countinuous:
    print("yes")
    print("reverse", counter[0] + 1, counter[len(counter) - 1] + 2)
else:
    print("no")


