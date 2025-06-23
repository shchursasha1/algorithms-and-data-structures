def f(n):
    sum = 0                   # O(1)
    for i in range(1, n + 1): # O(n)
        sum = sum + i         # O(n)
    return sum                # O(1)

#res: O(1)

#res of f(n): (1 + 2 + 3 + ... + n) = n * (n + 1) // 2

#optimized function:
def new_f(n):
    return n * (n + 1) // 2  # O(1)