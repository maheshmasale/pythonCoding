def combinationSum3( k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    def check_combinations(results, current, n, k, path):
        if n < 0 or k < 0 or (n > 0 and k == 0):
            return
        if n == 0 and k == 0:
            results.append(path[:])
            return
        for x in range(current, 10):
            if n - x < 0:
                break

            path.append(x)
            check_combinations(results, x + 1, n - x, k - 1, path)
            path.pop()

        return results

    return check_combinations([], 1, n, k, [])

print(combinationSum3(3,9))