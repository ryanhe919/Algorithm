
# 递归

def fib_1(n):
    return n if n == 0 or n == 1 else fib_1(n - 1) + fib_1(n - 2)

# 迭代

def fib_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    n_1 = 0
    n_2 = 1
    for i in range(n - 1):
        result = n_1 + n_2
        n_1 = n_2
        n_2 = result
    return result 