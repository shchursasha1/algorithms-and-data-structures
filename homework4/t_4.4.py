import math
# На відрізку [1.6, 3] знайдіть корінь рівняння sin 𝑥 = 𝑥 / 3.

def f(x):
    return math.sin(x) - x / 3

def solve(c, a, b):
    eps = 1e-7
    l, r = a, b
    while r - l > eps:
        m = (l + r) / 2.0
        if f(m) > c:
            l = m
        else:
            r = m
    return l

if __name__ == '__main__':
    print(f"Root = {solve(0, 1.6, 3):.6f}")