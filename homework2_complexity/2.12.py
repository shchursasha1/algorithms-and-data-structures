def f(n):                     # O(n)
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

#optimized function:
def optimized_f(n):           # O(1)
    return n * (n + 1) // 2

def g(n):                     # O(n^2)
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i + f(i)
    return sum

def optimized_g(n):                              # O(n)
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i + optimized_f(i)
    return sum

def h(n):
    return f(n) + g(n) # O(n) + O(n^2) = O(n^2)

def optimized_h(n):
    return optimized_f(n) + optimized_g(n) # O(1) + O(n) = O(n)