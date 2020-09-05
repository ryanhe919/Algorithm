def numWays(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    n_1 = 1
    n_2 = 2
    for i in range(n - 2):
        result = n_1 + n_2
        n_1 = n_2
        n_2 = result
    return result