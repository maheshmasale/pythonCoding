n, d = 9,5
c = [int(i) for i in "2 3 4 2 3 6 8 4 5".split()]
# print(n,d)
# print(c)
count = 0
if d == n:
    print(count)
else:
    x = sorted(c[:d + 1])
    c = x + c[d + 1:]
    # print(c)
    for i in range(d, len(c)):
        # x = sorted(c[i-d:i])
        x = c[i - d:i]
        # Find median of the given array!

        if d % 2 == 0:
            md = (x[d // 2] + x[(d // 2) + 1]) / 2
        else:
            md = x[d // 2 + 1]

        if 2 * md <= c[i]:
            count += 1
        # insert current item 'ith' in its location array
        for j in range(i - d + 1, i + 1):
            if c[j] > c[i]:
                print(c[:j], c[i],c[j:i],c[i + 1:])
                tempArr = c[:j]
                tempArr.append(c[i])
                c = tempArr + list(c[j:i]) + list(c[i + 1:])
                break

                # c = c[:i-d+1]+sorted(c[i-d+1:i+1])+c[i+1:]

    print(count)